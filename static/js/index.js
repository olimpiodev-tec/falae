function playAudio() {
  const text = document.getElementById("textInput").value;
  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
}

function downloadAudio() {
  const texto = document.getElementById('textInput').value;

  fetch('/text-to-audio', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: texto })
  })
  .then(response => response.json())
  .then(data => {
    const link = document.createElement('a');
    link.href = data.download_url;
    link.innerText = 'Clique aqui para baixar o áudio';
    link.download = '';
    document.body.appendChild(link);
  })
  .catch(err => {
    alert('Erro ao converter texto em áudio');
    console.error(err);
  });
}
