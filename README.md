# Medical Chatbot using Flask and Groq API

This is a Flask-based chatbot that responds to medical-related queries using the **Groq API**. If a user asks a non-medical question, the chatbot politely informs them that it can only answer medical-related queries.

## Features
- Uses **Groq API** to generate responses for medical queries.
- Implements **medical keyword filtering** to restrict responses to medical topics.
- Provides a **web interface** (`chat.html`) for user interaction.
- Returns **concise and efficient** medical responses.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)
- Langchain Groq API (`pip install langchain-groq`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/medical-chatbot.git
   cd medical-chatbot
