# 🤖 Buddy AI - Voice Assistant

Buddy AI is a lightweight Python voice assistant that leverages Gemini AI for intelligent voice interactions.

## ✨ Core Features

| Feature | Implementation |
|---------|---------------|
| 🎙️ Voice Commands | `speech_recognition` library |
| 🧠 AI Responses | Google Gemini API |
| 🔊 Voice Output | `pyttsx3` text-to-speech |
| 🔐 Secure Config | `.env` file management |

## 🛠️ Project Structure

```
buddy-ai/
├── talks.py               # Main application logic
└── .gitignore             # Ignored files pattern
```

## 🚀 Quick Setup

1. **Install dependencies**:
```bash
pip install pyttsx3 speechrecognition google-generativeai python-dotenv
```

2. **Configure API key**:
```bash
echo "GEMINI_API_KEY=your_key_here" > .env
```

3. **Run the assistant**:
```bash
python talks.py
```

## 💡 Usage Examples

```python
# Basic voice interaction flow:
1. Speak: "Open wikipedia"
2. Assistant opens wikipedia.org

3. Speak: "What's AI using Gemini"
4. Assistant provides Gemini-powered explanation
```

## 📌 Requirements

- Python 3.8+
- Working microphone
- Google Gemini API key
- Internet connection

## 🔧 Troubleshooting

If the assistant exits immediately:
1. Check microphone permissions
2. Verify your .env file exists
3. Ensure all packages are installed:
```bash
pip freeze | grep -E 'pyttsx3|speechrecognition|google-generativeai|python-dotenv'
```

## 🌟 Future Enhancements

- Add GUI interface
- Implement wake word detection
- Support for more music platform

## Security

- Never commit your .env file with API keys to GitHub.

- Add .env to your .gitignore file:

```bash
.env
```
