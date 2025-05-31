function convertTTS() {
    const text = document.getElementById("inputText").value;
    fetch('/tts', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: text})
    })
    .then(response => response.blob())
    .then(blob => {
        const audioPlayer = document.getElementById("audioPlayer");
        audioPlayer.src = URL.createObjectURL(blob);
        audioPlayer.style.display = "block";
        audioPlayer.play();
    })
    .catch(err => alert("TTS error: " + err));
}

function summarize() {
    const text = document.getElementById("inputText").value;
    fetch('/summarize', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: text})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary").innerText = "Summary: " + (data.summary || "No summary.");
    })
    .catch(err => alert("Summarize error: " + err));
}

function convertBraille() {
    const text = document.getElementById("inputText").value;
    fetch('/braille', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: text})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("braille").innerText = "Braille: " + (data.braille || "No braille output.");
    })
    .catch(err => alert("Braille error: " + err));
}

