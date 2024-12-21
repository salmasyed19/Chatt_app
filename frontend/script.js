async function sendMessage() {
    const message = document.getElementById("message").value;
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ message: message, sender: 1, receiver: 2 })
    });
    const result = await response.json();
    if (response.ok) {
        document.getElementById('chat-room').innerHTML += `<p>${result.message}</p>`;
    } else {
        alert('Failed to send message');
    }
}
