import streamlit as st 
import nltk
import os
import google.generativeai as genai
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

#Secure API key using environment varibales
API_KEY=os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY environment variable not set")

#Set your Gemini api key
genai.configure(api_key=API_KEY)

chatbot = genai.GenerativeModel('gemini-pro')

def healthcare_chatbot(user_input):
    if "appointment" in user_input:
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

    else:
        response = chatbot.generate_content(user_input)
        return response.text

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