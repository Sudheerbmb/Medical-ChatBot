# Medical Chatbot using Flask and Groq API  

## Table of Contents  

1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Installation](#installation)  
5. [Configuration](#configuration)  
6. [Usage](#usage)  
7. [API Endpoints](#api-endpoints)  
8. [Project Structure](#project-structure)  
9. [License](#license)  

---

## Introduction  

This is a simple **Flask-based medical chatbot** that uses the **Groq API** for natural language processing (NLP). The chatbot **only responds to medical-related queries** and politely declines non-medical questions.  

---

## Features  

| Feature | Description |  
|---------|------------|  
| **Flask Web Application** | A simple frontend to chat with the bot |  
| **Groq API Integration** | Uses `llama-3.1-8b-instant` model for responses |  
| **Medical Query Filtering** | Only processes queries related to healthcare |  
| **JSON Responses** | Returns chatbot responses in JSON format |  
| **Error Handling** | Provides polite messages for unsupported queries |  

---

## Technologies Used  

| Technology | Purpose |  
|------------|---------|  
| **Python** | Backend scripting |  
| **Flask** | Web framework |  
| **Groq API** | AI model for medical chatbot responses |  
| **HTML/CSS** | Frontend for chatbot interface |  

---

## Installation  

### Prerequisites  

- Python 3.x installed  
- Virtual environment (optional but recommended)  
- Flask and dependencies installed  

### Steps  

1. Clone the repository:  

   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
