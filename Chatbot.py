import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Fis Chatbot - Demo",
    page_icon=":robot:"
)

API_URL = '123'
headers = {"Authorization": 123}

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


st.title("FIS Chatbot")

st.write("Hey, welcome to the FIS chatbot beta! You can ask me a question below.")

user_input = get_text()

if user_input:
    # output = query({
    #    "inputs": {
    #        "past_user_inputs": st.session_state.past,
    #        "generated_responses": st.session_state.generated,
    #        "text": user_input,
    #    },"parameters": {"repetition_penalty": 1.33},
    #})

    st.session_state.past.append(user_input)
    st.session_state.generated.append('Fuck off!')

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')