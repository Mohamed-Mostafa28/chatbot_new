import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to set up the app UI
def setup_ui():
    st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
    st.title("Medical Chatbot 🧠")
    st.markdown("This is a chatbot built to help Doctors!")
    load_custom_css()

# Function to load custom CSS for chat styling, ensuring long messages wrap to multiple lines
def load_custom_css():
    st.markdown(
        """
        <style>
        .user-message, .bot-message {
            background-color: black;
            color: white;
            border-radius: 5px;
            padding: 8px;
            margin: 5px 0;
            text-align: left;
            word-wrap: break-word;  /* Ensure text wraps in both user and bot messages */
            white-space: pre-wrap;  /* Preserve whitespace and wrap text */
        }
        .bot-message {
            background-color: #444;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to generate a response (replace with actual API call)
def generate_response(prompt):
    return f"Bot: This is a dummy response for: '{prompt}'"

# Function to handle user input and update chat history
def handle_user_input():
    user_input = st.text_input("You: ", "")
    if st.button("Send") and user_input:
        st.session_state.messages.append(f"You: {user_input}")
        #---------------------------------------------
        response = generate_response(user_input)
        #---------------------------------------------
        st.session_state.messages.append(response)
    return user_input

# Function to display chat messages with proper wrapping
def display_chat_history():
    conversation = []
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message.startswith("You:"):
                st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message">{message}</div>', unsafe_allow_html=True)
            conversation.append(message)
    return conversation

# Function to clear chat history
def clear_chat():
    if st.button("Clear Chat"):
        st.session_state.messages = []


