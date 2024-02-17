import pandas as pd
import streamlit as st
import openai

st.title("DHV Startup Demo to Talk with Excel")
# Load the CSV data
data = pd.read_csv('data.csv')

uploaded_file = st.file_uploader("อัปโหลดไฟล์ตาราง Excel or CSV", type=["xlsx", "csv"])

# Load the uploaded file if available
data = None
if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    if file_extension == "xlsx":
        data = pd.read_excel(uploaded_file)
    elif file_extension == "csv":
        data = pd.read_csv(uploaded_file)

# Create a Streamlit app

st.title("ตารางข้อมูล")
st.write(data)

# Find the average of a specific column
#average = data['Marital'].mean()

# Set your API key
openai.api_key = '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'

# Initialize conversation history
conversation = []

# Define function to query GPT-3
def query_gpt3(message):
    conversation.append(f"User: {message}")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt='\n'.join(conversation),
        temperature=0.5,
        max_tokens=800,
        n=1,
        stop=None,
        #temperature_schedule=None,
        #log_level=None,
        logprobs=None,
        echo=False,
        #logit_bias=None
    )
    conversation.append(f"GPT-3: {response.choices[0].text.strip()}")
    return response.choices[0].text.strip()

# Create a Streamlit app

user_input = st.text_input("โปรดถามคำถาม: ")
if st.button("กดถาม"):
    if user_input:
        response = query_gpt3(user_input)
        st.write("AI ตอบ:", response)