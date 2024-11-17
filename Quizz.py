import streamlit as st
from g4f.client import Client

st.title("Customize Your Quiz and Get Recommendations!")
st.subheader("Add or remove questions to personalize your experience.")

questions = st.multiselect(
    "Select the questions you want to answer:",
    ["Preferred climate", "Preferred sunny days", "Preferred salary", "Preferred environment"]
)

prompt_parts = []

if "Preferred climate" in questions:
    climate = st.radio("Preferred climate", ("Warm", "Cold", "Moderate"))
    prompt_parts.append(f"a {climate} climate")
    
if "Preferred sunny days" in questions:
    sunny_days = st.slider("Prefer more sunny or cloudy days?", 0, 100, 50)
    prompt_parts.append(f"{sunny_days}% sunny days")
    
if "Preferred salary" in questions:
    salary = st.number_input("Preferred average salary (in USD)", min_value=1000, max_value=200000, step=500)
    prompt_parts.append(f"a salary of {salary} USD")
    
if "Preferred environment" in questions:
    nature = st.radio("Preferred environment", ("Mountains", "Beaches", "Cities", "Forests"))
    prompt_parts.append(f"{nature} environment")

custom_input = st.text_area("You can provide additional prefrences of the country you want to live in:")

if st.button("Get Country Recommendations"):
    if custom_input:
        custom_prompt = "I want to live in a country with " + ", ".join(prompt_parts) + "." + custom_input
    else:
        custom_prompt = "I want to live in a country with " + ", ".join(prompt_parts) + "." 
        
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": custom_prompt}],
        temperature=0.7,  
        max_tokens=100    
    )
    
    st.write("Prompt: ", custom_prompt)

    st.subheader("Your Top Country Recommendations:")
    
    st.write(response.choices[0].message.content)
