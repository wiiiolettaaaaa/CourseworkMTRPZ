async function generatePassword() {
    const length = document.getElementById('length').value;
    const digits = document.getElementById('digits').checked;
    const symbols = document.getElementById('symbols').checked;
    const uppercase = document.getElementById('uppercase').checked;
    const lowercase = document.getElementById('lowercase').checked;

    const response = await fetch(`/generate?length=${length}&digits=${digits}&symbols=${symbols}&uppercase=${uppercase}&lowercase=${lowercase}`);
    const data = await response.json();

    if (data.password) {
        document.getElementById('result').innerHTML = "<strong>Generated Password:</strong> " + data.password;
        loadHistory();
    } else {
        document.getElementById('result').innerText = "Error: " + data.error;
    }
}

async function loadHistory() {
    const response = await fetch('/history');
    const data = await response.json();

    if (data.history && data.history.length > 0) {
        document.getElementById('history').innerHTML = data.history.join("<br>");
    } else {
        document.getElementById('history').innerText = "No history yet.";
    }
}

window.onload = loadHistory;