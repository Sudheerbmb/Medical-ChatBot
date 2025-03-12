from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq  # Import the ChatGroq API

app = Flask(__name__)

# Groq API Key and Model Configuration
groq_api_key = "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"
model_name = "llama-3.1-8b-instant"
 # Replace with the desired model name

# Initialize the ChatGroq API client
llm = ChatGroq(api_key=groq_api_key, model=model_name)

# Define the instruction for the chat
instruction = "In this chat, respond to medical-related queries only. If the query is not medical-related, please respond with a polite message stating that I can only answer medical questions."

# List of medical-related keywords to identify if the query is related to medical topics
medical_keywords = [
    'doctor', 'medicine', 'health', 'symptom', 'treatment', 'diagnosis', 
    'therapy', 'medical', 'hospital', 'clinic', 'pharmacy', 'nurse', 
    'emergency', 'surgery', 'physician', 'prescription', 'patient', 
    'healthcare', 'pediatrician', 'dermatologist', 'gynecologist', 
    'cardiologist', 'neurologist', 'oncologist', 'radiologist', 
    'psychiatrist', 'ophthalmologist', 'orthopedic', 'dietitian', 
    'allergist', 'chiropractor', 'podiatrist', 'medication', 'delivery', 
    'order', 'track', 'shipment', 'customer service', 'pharmacy network', 
    'health advice', 'emergency assistance', 'drug recall', 'side effects', 
    'health tips', 'medication reminder', 'privacy', 'compliance', 'regulation', 
    'data privacy', 'healthcare provider', 'first aid', 'health guide', 
    'medicine availability', 'online pharmacy', 'prescription refill', 
    'pharmacy support', 'medication information', 'drug interaction', 
    'drug safety', 'medical emergency', 'pharmacy services', 'drug delivery', 
    'medical delivery', 'patient support', 'order status', 'payment options', 
    'drug compatibility', 'pharmaceutical care', 'patient care', 'medicine use', 
    'healthcare advice', 'prescription advice', 'medication order', 'prescription order', 
    'medication guidance', 'pharmacy assistance', 'healthcare support',
    'consultation', 'doctor consultation', 'medical advice', 'health consultation', 
    'telemedicine', 'virtual consultation', 'medical specialist', 'doctor appointment', 
    'online doctor', 'specialist consultation', 'second opinion', 'health specialist', 
    'medical consultation', 'physician consultation', 'GP consultation', 'doctor visit', 
    'health check', 'medical opinion', 'medical referral', 'remote consultation',
    'lab test', 'blood test', 'urine test', 'diagnostic test', 'pathology', 
    'laboratory', 'lab technician', 'test result', 'lab procedure', 
    'medical test', 'clinical test', 'biopsy', 'culture test', 'genetic test', 
    'microbiology test', 'serology test', 'immunology test', 'radiology test', 
    'PCR test', 'MRI scan', 'CT scan', 'X-ray', 'ultrasound'
]

@app.route('/chat')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = str(request.form['messageText'])
    
    # Check if the query is medical-related
    if not is_medical_query(user_message):
        bot_response_text = "I'm sorry, I can only answer medical-related questions. Please ask a question related to medical topics."
    else:
        # Send the query to the Groq API
        prompt = f"Respond to the following medical query: {user_message}. Please provide concise yet efficient output. Don't give in markdown format."
        
        response = llm.invoke(prompt)
        
        # Get the response from the Groq API
        if response:
            bot_response_text = response.content
        else:
            bot_response_text = "Sorry, I couldn't find a relevant response at this moment."

    # Return the response as JSON
    return jsonify({'status': 'OK', 'answer': bot_response_text})

def is_medical_query(query):
    """Check if the query is related to medical topics."""
    return any(keyword in query.lower() for keyword in medical_keywords)

if __name__ == '__main__':
    app.run(debug=True)
