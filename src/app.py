from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from dotenv import load_dotenv
import openai
import os
import uuid
from models.message import Message
from models.message_dao import MessageDAO


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('SECRET_KEY')

message_dao = MessageDAO(app.config['MONGO_URI'], os.getenv('MONGO_DB'))


@app.route('/')
def chat_window():
    # Use session ID as conversation ID
    if 'conversation_id' not in session:
        session['conversation_id'] = str(uuid.uuid4())
    messages = message_dao.get_all(session['conversation_id'])
    return render_template('chat_window.html', messages=messages)


@app.route('/send', methods=['POST'])
def send():
    # Get message content from form
    user_message_content = request.form.get('message')

    # Create user's message
    user_message = Message(None, 'user', user_message_content, session['conversation_id'])
    message_dao.create(user_message)

    # Send message to GPT-3 model
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": m.role,
                "content": m.content
            }
            for m in message_dao.get_all(session['conversation_id'])
        ]
    )

    # Create assistant's message
    assistant_message_content = completion.choices[0].message['content']
    assistant_message = Message(None, 'assistant', assistant_message_content, session['conversation_id'])
    message_dao.create(assistant_message)

    return jsonify({"role": "assistant", "message": assistant_message.__dict__})


@app.route('/clear', methods=['POST'])
def clear():
    message_dao.delete_all(session['conversation_id'])
    session.pop('conversation_id', None)
    return redirect(url_for('chat_window'))


if __name__ == '__main__':
    app.run(debug=True)
