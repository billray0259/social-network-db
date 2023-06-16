$(document).ready(function () {

    // AJAX function to send message
    function sendMessage(userMessageContent) {
        return $.ajax({
            url: '/send',
            type: 'POST',
            data: {
                message: userMessageContent
            }
        });
    }

    // AJAX function to clear chat
    function clearChat() {
        return $.ajax({
            url: '/clear',
            type: 'POST'
        });
    }

    // Event handler for chat form submission
    $('#chat-form').on('submit', function (e) {
        e.preventDefault();
        var userMessageContent = $('#message-input').val();
        
        // Immediately add user's message to chat window
        var userMessageElement = $('<div class="message outgoing"><div class="alert alert-primary" role="alert"></div></div>');
        userMessageElement.find('.alert').text(userMessageContent);
        $('.chat-container').append(userMessageElement);
        // Scroll to the bottom of the chat window
        $('.chat-container').scrollTop($('.chat-container')[0].scrollHeight);
        // Show typing animation
        $('#typing').addClass('active');

        sendMessage(userMessageContent).then(function(data) {
            // Hide typing animation
            $('#typing').removeClass('active');
            // Add assistant's message to chat window
            var assistantMessageElement = $('<div class="message incoming"><div class="alert alert-secondary" role="alert"></div></div>');
            assistantMessageElement.find('.alert').text(data.message.content);
            $('.chat-container').append(assistantMessageElement);
            // Scroll to the bottom of the chat window
            $('.chat-container').scrollTop($('.chat-container')[0].scrollHeight);
        });

        // Clear input field
        $('#message-input').val('');
    });

    // Event handler for the clear chat button
    $('#clear-chat').on('click', function () {
        clearChat().then(function(data) {
            // Remove all messages from the chat window
            $('.chat-container').empty();
        });
    });
});

$('#chat-button').on('click', function () {
    $('#chat-window').toggleClass('hidden');
});