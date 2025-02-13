import streamlit as st 
import nltk
from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "I'm not a doctor, but if you're experiencing symptoms, it's best to consult a medical professional .Please see a doctor for an accurate diagnosis based on your symptoms. Symptoms can vary. A doctor would be the best person to assess them."
    elif "appointment" in user_input:
        return "Would you like me to help you schedule an appointment with the doctor? Let me know if you'd like to book a doctor's appointment. Do you need help scheduling an appointment with a medical professional?"
    elif "medication" in user_input:
        return "Always follow your doctor’s prescription for medications. If you have concerns about your medication, consult your doctor.Taking prescribed medicines as directed is important for recovery."
    elif "diagnosis" in user_input:
        return "A proper diagnosis requires a doctor’s expertise. Please visit a healthcare provider for an accurate diagnosis. A medical professional can give you the best diagnosis."
    
    elif "prescription" in user_input:
        return "Only a doctor can provide a valid prescription. For a proper prescription, consult a certified healthcare provider. Medication should only be taken as prescribed by a doctor."
    elif "emergency" in user_input:
        return  "Please contact emergency services immediately! If it's a medical emergency, dial emergency services or visit a hospital. In an emergency, seek immediate medical attention."
    elif "follow-up" in user_input:
        return "A follow-up appointment is important for monitoring your health. Please schedule a follow-up as recommended by your doctor. Following up with your doctor ensures proper care."
    
    elif "advice" in user_input:
        return "It's best to consult a doctor for reliable medical advice. For expert advice, please talk to a healthcare professional. A doctor can provide the best guidance for your health concerns."
    
    elif "test" in user_input:
        return "Medical tests should be scheduled as per a doctor's recommendation. Would you like help in scheduling a medical test? Diagnostic tests are important for proper evaluation. Consult a doctor."
    elif "surgery" in user_input:
        return "A surgery recommendation should come from a qualified surgeon. If you need surgery, consult a medical specialist for details. A doctor can assess whether surgery is necessary."
    elif "treatment" in user_input:
        return "Only a healthcare provider can recommend proper treatment. For treatment options, please speak to a doctor. Medical treatment should be tailored to individual needs by a professional."
    
    elif "allergies" in user_input:
        return  "Allergy management should be guided by a doctor. If you're experiencing allergic reactions, consult a specialist. A doctor can suggest the best way to handle allergies."
    elif "immunization" in user_input:
        return "Vaccines are essential for immunity. Consult a healthcare provider for guidance. Would you like to know more about recommended immunizations? Staying up-to-date with immunizations helps prevent illnesses."
    elif "vaccination" in user_input:
        return "Please consult the Doctor for accurate vaccination recommendations"
    
    elif "health" in user_input:
        return  "Maintaining a balanced diet, regular exercise, and proper sleep is key to good health. Good health starts with a healthy lifestyle. Eat well, stay active, and manage stress. Routine medical checkups help ensure you stay in good health. Staying hydrated and getting enough rest are essential for overall well-being. Your mental and physical health are equally important - take care of both!"
    
    elif "diet" in user_input:
        return  "A balanced diet is important for health. A nutritionist can provide personalized advice. Healthy eating is key to wellness. Consult a doctor for dietary recommendations. A proper diet plan should be based on individual health needs."
    
    elif "exercise" in user_input:
        return "Regular exercise benefits overall health. A fitness expert or doctor can help. Staying active is important, but consult a professional for the right exercise plan. Exercise routines should be based on your health condition and fitness level."
    
    elif "sleep" in user_input:
        return "Getting 6-8 hours of sleep is essential for good health. If you're having trouble sleeping, try maintaining a regular sleep schedule. Avoid screens before bedtime and create a relaxing routine for better sleep."
    elif "stress" in user_input:
        return "Managing stress is important for overall well-being. A therapist or doctor can help. Stress-relief techniques like meditation or exercise can be beneficial. If stress is overwhelming, consider speaking to a professional."
    
    elif "anxiety" in user_input:
        return "If anxiety is affecting your daily life, please seek professional guidance. Anxiety management techniques include therapy, exercise, and relaxation methods. For persistent anxiety, it's best to consult a mental health specialist."
    elif "insurance" in user_input:
        return "For medical insurance details, please contact your provider."
    elif "pain" in user_input:
        return "If you're experiencing pain, consult a doctor for proper evaluation."
    elif "emergency" in user_input:
        return "If this is a medical emergency, please call emergency services immediately."
    elif "cold" in user_input:
        return "If you have a cold, stay hydrated, rest well, and consider warm fluids. Common cold symptoms usually resolve in a few days. If symptoms persist, see a doctor. A warm drink with honey and lemon can help soothe a sore throat due to a cold. If you have a runny nose and congestion, steam inhalation might provide relief."
    elif "fever" in user_input:
        return "If you have a fever, stay hydrated and get plenty of rest. A fever may indicate an infection. If it persists, consult a doctor. Taking a lukewarm bath and staying hydrated can help manage a mild fever. If your fever is above 102°F (39°C) or lasts more than three days, seek medical advice."
    elif "cough" in user_input:
        return "For a dry cough, try warm fluids and honey-based remedies. If your cough persists for more than two weeks, consult a doctor. A persistent cough may indicate an infection. Seek medical advice if needed. Try avoiding cold drinks and allergens if you have a cough."
    elif "headache"in user_input:
        return "For headaches, try resting in a quiet, dark room and staying hydrated. If you have frequent headaches, consider tracking triggers like stress, dehydration, or screen time. A cold or warm compress on the forehead can help relieve headaches. If headaches are severe or persistent, consult a doctor for further evaluation."
    elif "back pain" in user_input:
        return "For back pain, try stretching, maintaining good posture, and using a heating pad. Rest and avoid heavy lifting if you have back pain. If it persists, consult a doctor. Poor posture and prolonged sitting can cause back pain. Try taking short breaks and stretching. If back pain is severe or accompanied by numbness, seek medical advice."
    elif "fatigue" in user_input:
        return "For fatigue, try a warm bath, stretching, and avoiding screen time. If fatigue persists, consult a doctor. Rest and avoid prolonged sitting or heavy lifting. If fatigue is severe, it may indicate a medical condition. Seek medical advice if needed."
    elif "stomach pain" in user_input:
        return "For mild stomach pain, try drinking warm water and avoiding heavy meals. If stomach pain is severe or persistent, consult a doctor for evaluation. Ginger tea and probiotics may help with digestion-related stomach pain. If you have sharp stomach pain with vomiting or fever, seek medical attention immediately."
    elif "throat pain" in user_input:
        return "For throat pain, try warm saltwater gargles and stay hydrated. Drinking warm tea with honey can help soothe a sore throat. Avoid cold drinks and speak less if you have throat pain. If throat pain lasts more than a week or worsens, consult a doctor."
    elif "hygiene food" in user_input:
        return "Eating fresh fruits, vegetables, and well-cooked meals helps maintain good health. Wash fruits and vegetables thoroughly before eating to remove dirt and bacteria. Avoid junk food and processed meals. Opt for home-cooked food for better hygiene. Stay hydrated with clean, filtered water and avoid street food to prevent infections. Maintain proper food storage and always check expiry dates before consumption."
    elif "healthy food" in user_input:
        return "A balanced diet includes fruits, vegetables, lean proteins, whole grains, and healthy fats. Eating a variety of colorful fruits and vegetables provides essential vitamins and minerals. Include foods rich in fiber, such as whole grains, nuts, and legumes, for better digestion. Stay hydrated by drinking plenty of water and reducing sugary beverages. Limit processed foods and opt for fresh, home-cooked meals for better nutrition."     
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Health Assistant Chatbot")
    user_input = st.text_input("How can I assist you today ?")
    
    if st.button("Submit"):
        if user_input:
            st.write("user:",user_input)
            with st.spinner("Processing your query.., Please wait..."):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:",response)
        else:
            st.write("Please enter a input to get a Response.")
    
main()