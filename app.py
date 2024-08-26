from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Generative AI API with the API key
API_KEY = 'AIzaSyCnHiPnc81WluNjSklL6lLR5FO_NbHRCfM'
genai.configure(api_key=API_KEY)

# Initialize the generative model and start the chat session
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Define the instruction and keywords for medical queries
instruction = "In this chat, respond to medical-related queries only. If the query is not medical-related, please respond with a polite message stating that I can only answer medical questions."
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
    
    if not is_medical_query(user_message):
        bot_response_text = "I'm sorry, I can only answer medical-related questions. Please ask a question related to medical topics."
    else:
        bot_response = chat.send_message(user_message)
        bot_response_text = bot_response.text
    
    return jsonify({'status': 'OK', 'answer': bot_response_text})

def is_medical_query(query):
    return any(keyword in query.lower() for keyword in medical_keywords)

if __name__ == '__main__':
    app.run(debug=True)
