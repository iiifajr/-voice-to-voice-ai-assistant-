# 🎙️ Voice Assistant — Talk to AI, Hear It Talk Back!

> Input. Think. Reply. All in English. All in one pipeline. 🌐✨

Ever wanted an AI that *understands* what you're asking and *talks back* in clear English audio? This project does exactly that, powered by cutting-edge LLM and speech synthesis tools.

---

## 🚀 What This Project Does

🎙️ **User Input** -> 📝 **Prompt Processing** -> 🤖 **AI-Generated Response (Cohere LLM)** -> 🔊 **Spoken Reply (gTTS)**

In just 3 seamless steps, your query becomes a full interactive voice experience with AI — no typing required!

---

## 🛠️ Tech Stack

| Stage | Tool | Why |
| :--- | :--- | :--- |
| 🎙️ **Input Processing** | Python Console Input / STT | Captures and formats user prompts accurately in English. |
| 🧠 **Text -> Response** | Cohere (`command-r-08-2024`) | State-of-the-art reasoning and conversational response generation. |
| 🗣️ **Text -> Speech** | gTTS | Fast, free, natural-sounding English voice synthesis. |

---

## ⚡ Quick Start

### 1️⃣ Install dependencies
pip install cohere gTTS

### 2️⃣ Get your Cohere API key
Sign up free at dashboard.cohere.com and grab your API key.

### 3️⃣ Set up environment variable
export COHERE_API_KEY="YOUR_ACTUAL_API_KEY"

### 4️⃣ Run the pipeline
python app.py

---

## 🧬 Run The Pipeline Step-by-Step

### Step 1: Input & Personalization
# Displays author introductory bio and exports intro audio
print(ABOUT_ME)
text_to_speech_english(ABOUT_ME, filename="intro.mp3")
user_text = input("Enter your message in English: ")

### Step 2: Generate AI Response
import cohere, os

co = cohere.Client(os.getenv("COHERE_API_KEY"))
response = co.chat(
    model="command-r-08-2024",
    message=user_text
)
reply_text = response.text

### Step 3: Text to Speech
from gtts import gTTS

tts = gTTS(text=reply_text, lang='en')
tts.save("response.mp3")

> 🎧 Play response.mp3 and hear your AI reply in English!

---

## 💻 Complete Python Source Code (`app.py`)

import os
import cohere
from gtts import gTTS

# Read the API key securely from environment variables
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Personal Introduction & About Me Section
ABOUT_ME = """
Hi! I'm Fajr Aldajani, a Full-Systems and Full-Stack Systems Engineer passionate about Robotics, Embedded Systems, and building technology that solves real-world problems.

My interests span several areas:
- Robotics and Control Systems: Designing bio-inspired robots, kinematic analysis, and advanced control loops.
- Embedded Systems and IoT: Developing firmware, hardware prototypes, and smart site automation solutions.
- Computer Vision and AI: Building intelligent object recognition pipelines and real-time image processing.
- Systems and Network Security: Engineering secure network architectures, access controls, and low-level kernel simulators.

I enjoy learning by building real projects and exploring the connection between hardware, low-level software, and artificial intelligence.
"""

def generate_response(prompt):
    """Send the user prompt to Cohere LLM and return the generated text response."""
    print(f"\nUser Query: {prompt}")
    
    # Active model endpoint
    response = co.chat(
        model="command-r-08-2024",
        message=prompt
    )
    
    answer = response.text
    print(f"AI Assistant Response: {answer}")
    return answer

def text_to_speech_english(text, filename="response.mp3"):
    """Convert text into an English speech audio file."""
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"\nAudio generated successfully! Saved as '{filename}'")

if __name__ == "__main__":
    # 1. Print and generate audio for Welcome & About Me message
    print("=" * 60)
    print(ABOUT_ME)
    print("=" * 60)
    
    # Generate speech for the introduction
    text_to_speech_english(ABOUT_ME, filename="intro.mp3")
    
    # 2. Get user input
    user_text = input("\nEnter your message in English: ")
    
    if user_text.strip():
        # Step 1: Generate AI response
        ai_response = generate_response(user_text)
        
        # Step 2: Convert AI response to audio
        text_to_speech_english(ai_response, filename="response.mp3")

---

## 📁 Project Structure

app.py           # Main pipeline code with full logic
requirements.txt # Project dependency list
README.md        # Complete documentation & report

---

## 🔮 Future Improvements

- [ ] Real-time speech-to-text streaming with RealtimeSTT
- [ ] Web / Mobile user interface (Gradio or Streamlit)
- [ ] Multi-turn conversation memory with LangChain
- [ ] Multi-language voice switching

---

## ⚠️ Note

Never commit your API key to GitHub! This project uses environment variables (os.getenv) to keep your keys safe from being exposed in public code. 🔑🔐

---

## 💡 Built With Curiosity

This project explores how accessible and powerful open-source & AI APIs have become — turning a simple concept into a functional voice-to-voice interaction pipeline.

Give it a ⭐ if you found it useful!

---

## 👥 Engineering Curation & Metadata

- **Lead Engineer:** Eng. Fajr Aldajani
- **Role:** Full-Systems & Full-Stack Systems Engineer
- **Core Technology Suite:** Python 3.x | Cohere LLM | gTTS | Git
- **Status:** Verified Production Build & Fully Deployed 🚀🏆🏁
