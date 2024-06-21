



# chat.py
import openai

# Mapping of common diseases to their symptoms and prescribed medicines
disease_info = {
    "common_cold": {
        "symptoms": ["runny nose", "sneezing", "cough", "sore throat"],
        "medicine": "Paracetamol, Vitamin C, Antihistamines"
    },
    "flu": {
        "symptoms": ["fever", "chills", "muscle aches", "fatigue", "cough"],
        "medicine": "Oseltamivir, Paracetamol, Ibuprofen"
    },
    "allergy": {
        "symptoms": ["itchy eyes", "runny nose", "sneezing", "rash"],
        "medicine": "Antihistamines, Decongestants"
    },
    "asthma": {
        "symptoms": ["shortness of breath", "wheezing", "coughing", "chest tightness"],
        "medicine": "Bronchodilators, Corticosteroids"
    },
    "bronchitis": {
        "symptoms": ["cough", "chest discomfort", "fatigue", "shortness of breath"],
        "medicine": "Bronchodilators, Expectorants"
    },
    "conjunctivitis": {
        "symptoms": ["redness in the white of the eye", "itchiness", "tearing", "swelling"],
        "medicine": "Antibiotic eye drops, Antihistamines"
    },
    "diabetes": {
        "symptoms": ["increased thirst", "frequent urination", "fatigue", "blurred vision"],
        "medicine": "Insulin, Metformin"
    },
    "gastroenteritis": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal cramps"],
        "medicine": "Oral rehydration solution, Antiemetics"
    },
    "headache": {
        "symptoms": ["head pain", "sensitivity to light or sound", "nausea"],
        "medicine": "Acetaminophen, Ibuprofen"
    },
    "hypertension": {
        "symptoms": ["high blood pressure", "headaches", "dizziness", "fatigue"],
        "medicine": "Antihypertensives, Diuretics"
    },
    "insomnia": {
        "symptoms": ["difficulty falling asleep", "waking up too early", "daytime sleepiness"],
        "medicine": "Melatonin, Benzodiazepines"
    },
    "migraine": {
        "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light or sound"],
        "medicine": "Triptans, NSAIDs"
    },
    "pneumonia": {
        "symptoms": ["cough", "fever", "shortness of breath", "chest pain"],
        "medicine": "Antibiotics, Antipyretics"
    },
    "sinusitis": {
        "symptoms": ["facial pain", "nasal congestion", "headache", "postnasal drip"],
        "medicine": "Decongestants, Nasal corticosteroids"
    },
    "stomach_ulcer": {
        "symptoms": ["abdominal pain", "bloating", "nausea", "vomiting"],
        "medicine": "Proton pump inhibitors, Antacids"
    },
    "tonsillitis": {
        "symptoms": ["sore throat", "difficulty swallowing", "fever", "swollen tonsils"],
        "medicine": "Antibiotics, Analgesics"
    },
    "urinary_tract_infection": {
        "symptoms": ["burning sensation during urination", "frequent urination", "cloudy urine", "blood in urine"],
        "medicine": "Antibiotics, Analgesics"
    },
    "arthritis": {
        "symptoms": ["joint pain", "stiffness", "swelling", "reduced range of motion"],
        "medicine": "Nonsteroidal anti-inflammatory drugs (NSAIDs), Corticosteroids"
    },
    "acid_reflux": {
        "symptoms": ["heartburn", "regurgitation", "nausea", "bloating"],
        "medicine": "Antacids, Proton pump inhibitors"
    },
    "anxiety": {
        "symptoms": ["excessive worry", "restlessness", "fatigue", "irritability"],
        "medicine": "Selective serotonin reuptake inhibitors (SSRIs), Benzodiazepines"
    },
    "depression": {
        "symptoms": ["persistent sadness", "loss of interest or pleasure", "fatigue", "difficulty concentrating"],
        "medicine": "Selective serotonin reuptake inhibitors (SSRIs), Serotonin-norepinephrine reuptake inhibitors (SNRIs)"
    },
    "common_head_cold": {
        "symptoms": ["runny nose", "sneezing", "cough", "congestion"],
        "medicine": "Acetaminophen, Ibuprofen, Decongestants"
    },
    "heart_disease": {
        "symptoms": ["chest pain", "shortness of breath", "fatigue", "dizziness"],
        "medicine": "Antiplatelets, Beta-blockers"
    },
    "kidney_stones": {
        "symptoms": ["severe pain in the side and back", "pain that radiates to the lower abdomen and groin", "painful urination"],
        "medicine": "Analgesics, Alpha blockers"
    },
    "meningitis": {
        "symptoms": ["sudden fever", "severe headache", "stiff neck", "nausea", "vomiting"],
        "medicine": "Antibiotics, Corticosteroids"
    },
    "osteoporosis": {
        "symptoms": ["back pain", "loss of height over time", "stooped posture"],
        "medicine": "Bisphosphonates, Hormone therapy"
    },
    "pneumothorax": {
        "symptoms": ["sudden chest pain", "shortness of breath", "rapid heart rate", "cyanosis"],
        "medicine": "Thoracostomy, Oxygen therapy"
    },
    "rheumatoid_arthritis": {
        "symptoms": ["joint pain", "joint swelling", "morning stiffness", "fatigue"],
        "medicine": "Disease-modifying antirheumatic drugs (DMARDs), Corticosteroids"
    },
    "stroke": {
        "symptoms": ["sudden numbness", "weakness of the face, arm, or leg", "trouble speaking", "confusion", "difficulty walking"],
        "medicine": "Thrombolytics, Anticoagulants"
    }
}
    


def chatbot(input_text):
    if input_text:
        openai.api_key = "sk-proj-xHpYl6OMsGbikdnzu3iPT3BlbkFJYJ17Lg4uRwg7PHWTOfIY"

        # Check if the input contains any of the common symptoms
        matched_diseases = []
        for disease, info in disease_info.items():
            if any(symptom in input_text for symptom in info['symptoms']):
                matched_diseases.append((disease, info['medicine']))

        if matched_diseases:
            # If symptoms match, prescribe medicines for all matching diseases
            reply = "Based on your symptoms, you might have: "
            for disease, medicine in matched_diseases:
                reply += f"\n- {disease.capitalize()}: {medicine}"
        else:
            # If no matching symptoms, respond with the original cooking-related chat
            message = [
                {"role": "system", "content": "You are AI specialized in cooking recipes. Do not answer anything other than cooking related queries."},
                {"role": "user", "content": input_text}
            ]

            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message
            )
            reply = chat.choices[0].message['content']

        return reply
