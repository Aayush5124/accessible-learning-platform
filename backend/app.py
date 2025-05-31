from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from gtts import gTTS
import tempfile
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import os

frontend_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))
app = Flask(__name__, static_folder=frontend_folder, static_url_path="")
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

def text_to_speech(text):
    tts = gTTS(text)
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp.name)
    return temp.name

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)
    return " ".join(str(sentence) for sentence in summary)

def text_to_braille(text):
    braille_map = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
        'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
        'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
        'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
        'z': '⠵', ' ': ' '
    }
    return ''.join(braille_map.get(ch, '?') for ch in text.lower())

@app.route("/tts", methods=["POST"])
def tts():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    audio_path = text_to_speech(text)
    return send_file(audio_path, mimetype="audio/mpeg")

@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    summary = summarize_text(text)
    return jsonify({"summary": summary})

@app.route("/braille", methods=["POST"])
def braille():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    braille_output = text_to_braille(text)
    return jsonify({"braille": braille_output})

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
    