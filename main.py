# import streamlit as st
# import google.generativeai as genai
# import pandas as pd
# import datetime

# # --- Set up Gemini API ---
# genai.configure(api_key="AIzaSyDgGYre8fT50KhnHC-Pm10RZdegKshlXr8")

# model = genai.GenerativeModel('gemini-flash')

# # --- Page Setup ---
# st.set_page_config(page_title="Auto Insurance AI Agent", layout="centered")
# st.title("🚗 Auto Insurance Virtual Agent")

# st.markdown("Hi! I'm your AI Assistant. Please answer a few questions to check your eligibility.")

# # --- Form ---
# with st.form("insurance_form"):
#     name = st.text_input("Your Name")
#     car_model = st.text_input("Car Make & Model")
#     zip_code = st.text_input("ZIP Code")
#     driving_years = st.number_input("Years of Driving Experience", min_value=0, max_value=50)
#     clean_record = st.radio("Do you have a clean driving record?", ["Yes", "No"])
#     currently_insured = st.radio("Are you currently insured?", ["Yes", "No"])
#     submitted = st.form_submit_button("Check Eligibility")

# # --- Process form ---
# if submitted:
#     user_input = f"""
#     Name: {name}
#     Car: {car_model}
#     ZIP: {zip_code}
#     Experience: {driving_years} years
#     Clean Record: {clean_record}
#     Currently Insured: {currently_insured}
#     """

#     with st.spinner("Checking eligibility..."):
#         prompt = f"""
#         Based on the following auto insurance lead, respond with a polite message if they qualify for a special insurance plan. Keep it short.

#         {user_input}
#         """
#         response = model.generate_content(prompt)
#         st.success("✅ AI Response:")
#         st.write(response.text)

#         # Save to CSV (or later Google Sheet)
#         df = pd.DataFrame([{
#             "Timestamp": datetime.datetime.now(),
#             "Name": name,
#             "Car Model": car_model,
#             "ZIP": zip_code,
#             "Experience": driving_years,
#             "Clean Record": clean_record,
#             "Insured": currently_insured,
#             "Response": response.text
#         }])

#         df.to_csv("leads.csv", mode="a", index=False, header=False)
#         st.success("Lead saved successfully ✅")















# import os
# import datetime
# import pandas as pd
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # --- Load environment variables ---
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Use free Gemini model
# model = genai.GenerativeModel("models/gemini-1.5-flash")

# # --- Streamlit Page Setup ---
# st.set_page_config(page_title="Auto Insurance AI Agent", layout="centered")
# st.title("🚗 Auto Insurance Virtual Agent")
# st.markdown("Hi! I'm your AI Assistant. Please answer a few questions to check your eligibility.")

# # --- Form ---
# with st.form("insurance_form"):
#     name = st.text_input("Your Name")
#     car_model = st.text_input("Car Make & Model")
#     zip_code = st.text_input("ZIP Code")
#     driving_years = st.number_input("Years of Driving Experience", min_value=0, max_value=50)
#     clean_record = st.radio("Do you have a clean driving record?", ["Yes", "No"])
#     currently_insured = st.radio("Are you currently insured?", ["Yes", "No"])
#     submitted = st.form_submit_button("Check Eligibility")

# # --- Process form ---
# if submitted:
#     user_input = f"""
#     Name: {name}
#     Car: {car_model}
#     ZIP: {zip_code}
#     Experience: {driving_years} years
#     Clean Record: {clean_record}
#     Currently Insured: {currently_insured}
#     """

#     with st.spinner("Checking eligibility..."):
#         prompt = f"""
#         Based on the following auto insurance lead, respond with a polite message 
#         if they qualify for a special insurance plan. Keep it short.

#         {user_input}
#         """
#         response = model.generate_content(prompt)

#         st.success("✅ AI Response:")
#         st.write(response.text)

#         # Save to CSV
#         df = pd.DataFrame([{
#             "Timestamp": datetime.datetime.now(),
#             "Name": name,
#             "Car Model": car_model,
#             "ZIP": zip_code,
#             "Experience": driving_years,
#             "Clean Record": clean_record,
#             "Insured": currently_insured,
#             "Response": response.text
#         }])
#         df.to_csv("leads.csv", mode="a", index=False, header=False)
#         st.success("Lead saved successfully ✅")










import os
import datetime
import pandas as pd
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use free Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Auto Insurance AI Agent", layout="centered")
st.title("🚗 Auto Insurance Virtual Agent")
st.markdown("Hi! I'm your AI Assistant. Please answer a few questions to check your eligibility.")

# --- Form ---
with st.form("insurance_form"):
    name = st.text_input("Your Name")
    car_model = st.text_input("Car Make & Model")
    zip_code = st.text_input("ZIP Code")
    driving_years = st.number_input("Years of Driving Experience", min_value=0, max_value=50)
    clean_record = st.radio("Do you have a clean driving record?", ["Yes", "No"])
    currently_insured = st.radio("Are you currently insured?", ["Yes", "No"])
    submitted = st.form_submit_button("Check Eligibility")

# --- Process form ---
if submitted:
    user_input = f"""
    Name: {name}
    Car: {car_model}
    ZIP: {zip_code}
    Experience: {driving_years} years
    Clean Record: {clean_record}
    Currently Insured: {currently_insured}
    """

    with st.spinner("Checking eligibility..."):
        prompt = f"""
        Based on the following auto insurance lead, respond with a polite message 
        if they qualify for a special insurance plan. Keep it short.

        {user_input}
        """
        response = model.generate_content(prompt)

        st.success("✅ AI Response:")
        st.write(response.text)

        # Save to CSV
        df = pd.DataFrame([{
            "Timestamp": datetime.datetime.now(),
            "Name": name,
            "Car Model": car_model,
            "ZIP": zip_code,
            "Experience": driving_years,
            "Clean Record": clean_record,
            "Insured": currently_insured,
            "Response": response.text
        }])
        df.to_csv("leads.csv", mode="a", index=False, header=False)
        st.success("Lead saved successfully ✅")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Made by <b>Alishba Rehman</b></p>",
    unsafe_allow_html=True
)
