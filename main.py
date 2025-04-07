from flask import Flask, request, render_template, send_from_directory, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

AUDIO_FOLDER = 'static/audio'
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/text-to-audio', methods=['POST'])
def text_to_audio():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Texto não fornecido'}), 400

    # Nome único para o arquivo
    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    # Gera o áudio
    tts = gTTS(text=text, lang='pt', slow=False)
    tts.save(filepath)

    # Retorna o link para download
    download_url = f"/download/{filename}"
    return jsonify({'download_url': download_url})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(AUDIO_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)