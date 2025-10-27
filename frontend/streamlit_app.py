import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_URL = os.getenv('API_URL')  

st.title('RAG Assistant')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question about your documents"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner('Querying...'):
           
            response = requests.post(API_URL, json={'question': prompt})
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer')
                st.markdown(answer)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                error_msg = f'API error: {response.status_code} - {response.text}'
                st.error(error_msg)
                # Add error to chat history
                st.session_state.messages.append({"role": "assistant", "content": error_msg})