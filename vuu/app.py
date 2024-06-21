from flask import Flask, render_template, request, jsonify
from chat import chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    user_message = str(request.form['messageText'])

    # If user message is empty, ask for symptoms
    if not user_message:
        return jsonify({'status': 'OK', 'answer': "Hello! I'm here to help you with any health concerns. Could you please tell me about your symptoms?"})

    # If user asks for health tips, provide some tips
    if user_message.lower() == 'health tips':
        tips = [
            "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
            "Stay hydrated by drinking plenty of water throughout the day.",
            "Engage in regular physical activity to keep your body and mind healthy.",
            "Get enough sleep each night to support overall well-being.",
            "Manage stress through relaxation techniques like deep breathing or meditation.",
            "Avoid smoking and limit alcohol consumption to promote good health.",
            "Stay up to date with routine check-ups and screenings to prevent health issues.",
        ]
        return jsonify({'status': 'OK', 'answer': '\n'.join(tips)})

    # Pass user message to chatbot function
    bot_response = chatbot(user_message)

    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True, port=8765)
