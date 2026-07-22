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
