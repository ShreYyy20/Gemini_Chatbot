document.getElementById('chat-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const chatInput = document.getElementById('chat-input');
    const message = chatInput.value;
    const chatBox = document.getElementById('chat-box');

    // Send the message to the server
    const response = await fetch('/send_message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Clear the chat box
    chatBox.innerHTML = '';

    // Display the last three messages
    data.last_messages.forEach(msg => {
        const userMessage = document.createElement('div');
        userMessage.textContent = `You: ${msg.user}`;
        chatBox.appendChild(userMessage);

        const botMessage = document.createElement('div');
        botMessage.textContent = `Bot: ${msg.bot}`;
        chatBox.appendChild(botMessage);
    });

    // Append the latest response
    const botMessage = document.createElement('div');
    botMessage.textContent = `Bot: ${data.response}`;
    chatBox.appendChild(botMessage);

    // Clear the input
    chatInput.value = '';
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
