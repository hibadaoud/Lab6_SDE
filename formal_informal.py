import streamlit as st
from g4f.client import Client

st.title("Customize Your Quiz and Get Recommendations!")
st.subheader("Add or remove questions to personalize your experience.")

# Allow users to select the questions they want to answer
questions = st.multiselect(
    "Select the questions you want to answer:",
    ["Preferred climate", "Preferred sunny days", "Preferred salary", "Preferred environment"]
)

# Create empty prompt sections
prompt_parts = []

# Collect input for the selected questions
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

if st.checkbox("Test different prompt structures?"):
    structure_type = st.radio("Choose a prompt structure:", ("Formal", "Conversational", "Simple"))
    
    if structure_type == "Formal":
        structured_prompt = f"I am seeking a country that provides {', '.join(prompt_parts)}."
    elif structure_type == "Conversational":
        structured_prompt = f"Hey, I am looking for a country with {', '.join(prompt_parts)}."
    else:
        structured_prompt = f"Country with {', '.join([part.split()[1] for part in prompt_parts])}."

# Generate the final prompt
if st.button("Get Country Recommendations"):
    
    # Call GPT-4 API using G4F library
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": structured_prompt}],
    )
    
    st.write("Prompt: ", structured_prompt)

    # Display the GPT-4 response
    st.subheader("Your Top Country Recommendations:")
    st.write(response.choices[0].message.content)
