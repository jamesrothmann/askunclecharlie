import openai
import streamlit as st
from streamlit_chat import message

# Set up the OpenAI API key
openai.api_key = st.secrets["api_secret"]

# Define the chatbot function
def chatbot(input_text):
    # Call the OpenAI Chat API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text},
            {"role": "assistant", "content": ""}
        ],
        max_tokens=100,
        temperature=0.5,
    )

    # Extract the generated response from the API response
    answer = response.choices[0].text.strip()
    
    return answer

# Creating the chatbot interface
st.title("Chatbot: OpenAI + Streamlit")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Get the user's input
input_text = st.text_input("You: ", "", key="input")

# Generate a response and store it
if input_text:
    output = chatbot(input_text)
    st.session_state['generated'].append(output)
    st.session_state['past'].append(input_text)

# Display the conversation
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
