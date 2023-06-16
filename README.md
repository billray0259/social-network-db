# Social Network DB
A note-taking app designed specifically for keeping track of the people in your life and understanding the people in their lives.

## Data architecture:

### Person
- _id (ObjectId)
- name (str)
  - The person's name: John Smith
- description (str)
  - Markdown document containing a description of this person
- data (dict)
  - JSON object containing arbitrary properties about this person: {'phone_number': ..., 'birthday': ..., 'hobbies': ...,}
- relationships (list[ObjectId])
  - List of Relationship ObjectId that connect this person to other persons

### Relationship
- _id (ObjectId)
- name (str)
  - The relationship's name: Friend
- description (markdown document)
  - Markdown document containing a description of this relationship
- data (dict)
  - JSON object contianing arbitrary properties about this relationship: {'since': ..., 'where': ..., 'how': ...,}
- Persons (list[ObjectId])
  - A list of length two containing the ObjectId of the two Persons that are connected by this Relationship

## User Interface
- User sends instructional/informational message to GPT model
- GPT model interprets message and updates the social network database to follow the instructions or be consistent with the information the user provided
  - GPT model uses functions to find related Persons/Relationships
  - GPT model uses functions to update the database
- User can view a graph with nodes and edges of the social network
- User can click on nodes and edges to view their descriptions as rendered markdown


## Tech Stack

- Flask
- MongoDB
- CytoScape.js
- OpenAI API


## File Structure

```
app.py
models
  - user.py
  - person.py
  - relationship.py
  - graph.py
  - gpt.py
  - db.py
  - __init__.py
templates
  - index.html