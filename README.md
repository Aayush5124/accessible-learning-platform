# Accessible Learning Platform

Accessible Learning Platform is a web application designed to make digital content more inclusive for everyone. It provides users with:

- **Text-to-Speech (TTS):** Instantly convert text into natural-sounding audio.
- **Summarization:** Generate concise summaries of long texts for easier understanding.
- **Braille Conversion:** Transform written text into Unicode Braille for visually impaired users.

The project is built using Python (Flask) for the backend and a modern, responsive frontend.  
Its goal is to support accessible education and communication for all users, regardless of their abilities.

## Features

- 🌎 **Inclusive:** Easy access to text, audio, and braille formats.
- 🗣️ **Text-to-Speech:** Listen to any text with a single click.
- ✂️ **Summarization:** Get quick summaries of long paragraphs.
- ⠿ **Braille:** Convert text for braille readers and learners.
- 🖥️ **Simple UI:** Clean, user-friendly interface.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aayush5124/accessible-learning-platform.git
   cd accessible-learning-platform
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` does not exist, install these manually:
   ```bash
   pip install flask flask-cors gTTS sumy numpy
   ```

   For summarization, you also need to install NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   ```

3. **Run the Flask backend**
   ```bash
   cd backend
   python app.py
   ```
   The server will start at [http://localhost:5000](http://localhost:5000).

4. **Open the frontend**
   - Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Project Structure

```
accessible-learning-platform/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```

## License

Open source—feel free to contribute!

---

> Made with ❤️ by [Aayush5124](https://github.com/Aayush5124)
