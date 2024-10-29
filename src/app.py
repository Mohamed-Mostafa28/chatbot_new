# # import streamlit as st
# # from dotenv import load_dotenv
# # from UiTemplate import *
# # from model import *
# # import os
# # from Create_Messages import *


# # Conversation = []
# # # Main function to run the app
# # def main():
# #     # Initialize session state if not already done
# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []  
    
# #     # Set up the app UI and input handling
# #     setup_ui()
# #     handle_user_input()
    
# #     # # Display conversation history
# #     # conversation = display_chat_history()

# #     # # Clear chat functionality
# #     # clear_chat()

# #     # # Debug: Print conversation history to console (optional)
# #     # print(conversation)
# #     # print("xxxxxxxx")

   
   
   
# #     # Conversation=[]
# #     SystemMessage = CreateSystemMessage(text="You are helper bot, you want to ask me some questions to find out my name and age and phone number and try to convince me and ask me agian and each question in one senetence and when you get all inmoframtion try to close this conversation")  
# #     Conversation.append(SystemMessage)
   
# #     #======================================================
# #     for i in range(15):

# #         ai_message = LLM_Model(Conversation)
# #         print(ai_message.content)  
        
# #         Conversation.append(CreateAIMessage(ai_message.content)) 
  
# # #   -----------------------------------------------------------
# #         text=input("You : ")
# #         if text == "exit":
# #             break
# #         HumanMessage = CreateHumanMessage(text=text)
# #         Conversation.append(HumanMessage)
# #   #   -----------------------------------------------------------
        
# #         print("*******************************************")

        





# # # Run the app
# # if __name__ == "__main__":
# #     main()


# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************

#     # """
#     # not bad when test it
    
#     # """
# # import streamlit as st
# # import os
# # from dotenv import load_dotenv
# # from UiTemplate import *
# # from model import *
# # from Create_Messages import *

# # # Load environment variables
# # load_dotenv()

# # # Function to set up the app UI
# # def setup_ui():
# #     st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
# #     st.title("Medical Chatbot 🧠")
# #     st.markdown("This is a chatbot built to help Doctors!")
# #     load_custom_css()

# # # Function to load custom CSS for chat styling, ensuring long messages wrap to multiple lines
# # def load_custom_css():
# #     st.markdown(
# #         """
# #         <style>
# #         .user-message, .bot-message {
# #             background-color: black;
# #             color: white;
# #             border-radius: 5px;
# #             padding: 8px;
# #             margin: 5px 0;
# #             text-align: left;
# #             word-wrap: break-word;
# #             white-space: pre-wrap;
# #         }
# #         .bot-message {
# #             background-color: #444;
# #         }
# #         </style>
# #         """,
# #         unsafe_allow_html=True
# #     )

# # # Function to handle user input and update chat history
# # def handle_user_input():
# #     user_input = st.text_input("You: ", "")
# #     if st.button("Send") and user_input:
# #         st.session_state.messages.append(f"You: {user_input}")
# #         HumanMessage = CreateHumanMessage(text=user_input)
# #         st.session_state.conversation.append(HumanMessage)
# #         return user_input
# #     return None

# # # Function to display chat messages with proper wrapping
# # def display_chat_history():
# #     conversation = []
# #     if st.session_state.messages:
# #         for message in st.session_state.messages:
# #             if message.startswith("You:"):
# #                 st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
# #             else:
# #                 st.markdown(f'<div class="bot-message">{message}</div>', unsafe_allow_html=True)
# #             conversation.append(message)
# #     return conversation



 
# # # Function to clear chat history
# # def clear_chat():
# #     if st.button("Clear Chat"):
# #         st.session_state.messages = []
# #         st.session_state.conversation = []

# # # Main function to run the app and interact with the LLM model
# # def main():
# #     # Initialize session state for messages and conversation if not already done
# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []
# #     if "conversation" not in st.session_state:
# #         st.session_state.conversation = []

# #     # Set up the app UI and input handling
# #     setup_ui()

# #     # Add the initial system message for the LLM
# #     if not st.session_state.conversation:
# #         SystemMessage = CreateSystemMessage(text="You are helper bot, you want to ask me some things to find out my name, age, and phone number")
# #         st.session_state.conversation.append(SystemMessage)

# #     # Handle user input and append to conversation
# #     user_input = handle_user_input()

# #     if user_input:
# #         # Generate AI message using the LLM model
# #         ai_message = LLM_Model(st.session_state.conversation)
# #         st.session_state.messages.append(f"Bot: {ai_message.content}")
        
# #         # Append the AI response to the conversation
# #         st.session_state.conversation.append(CreateAIMessage(ai_message.content))

# #     # Display conversation history
# #     display_chat_history()

# #     # Clear chat functionality
# #     clear_chat()
# #     print("****************************")

# # # Run the app
# # if __name__ == "__main__":
# #     main()



# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************
# #*****************************************************








# import streamlit as st
# from dotenv import load_dotenv
# from model import LLM_Model
# from Create_Messages import CreateHumanMessage, CreateAIMessage, CreateSystemMessage
# from prompt import *
# # Load environment variables
# load_dotenv()

# # Initialize session state for conversation and messages
# if "conversation" not in st.session_state:
#     st.session_state.conversation = []
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Set up the UI
# st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
# st.title("Medical Chatbot 🧠")
# st.markdown("This is a chatbot built to help Doctors!")

# # Load custom CSS for styling chat messages
# st.markdown("""
#     <style>
#     .user-message, .bot-message {
#         background-color: black;
#         color: white;
#         border-radius: 5px;
#         padding: 8px;
#         margin: 5px 0;
#         word-wrap: break-word;
#         white-space: pre-wrap;
#     }
#     .bot-message {
#         background-color: #444;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Add initial system message if conversation is empty
# if not st.session_state.conversation:

#     system_msg = CreateSystemMessage(text=All_QuestionsWithAllDataWithoutCommentsNewTemplte)
#     st.session_state.conversation.append(system_msg)

# # Handle user input and AI response
# user_input = st.text_input("You: ", "")
# if st.button("Send") and user_input:
#     st.session_state.messages.append(f"You: {user_input}")
#     human_msg = CreateHumanMessage(text=user_input)
#     st.session_state.conversation.append(human_msg)
    
#     # Generate AI response using the LLM model
#     ai_response = LLM_Model(st.session_state.conversation)
#     st.session_state.messages.append(f"Bot: {ai_response.content}")
#     st.session_state.conversation.append(CreateAIMessage(ai_response.content))

# # Display the conversation history
# for msg in st.session_state.messages:
#     if msg.startswith("You:"):
#         st.markdown(f'<div class="user-message">{msg}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="bot-message">{msg}</div>', unsafe_allow_html=True)



# # Clear chat history
# if st.button("Clear Chat"):
#     st.session_state.messages = []
#     st.session_state.conversation = []
    
    
   



from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from model import LLM_Model
from Create_Messages import CreateHumanMessage, CreateAIMessage, CreateSystemMessage
from prompt import All_QuestionsWithAllDataWithoutCommentsNewTemplte
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize session state for conversation and messages
conversation = []
messages = []

# Add initial system message to the conversation
if not conversation:
    system_msg = CreateSystemMessage(text=All_QuestionsWithAllDataWithoutCommentsNewTemplte)
    conversation.append(system_msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation, messages
    
    # Get user input from the form
    user_input = request.form['user_input']
    
    if user_input:
        # Add user's message to the messages
        messages.append(f"You: {user_input}")
        human_msg = CreateHumanMessage(text=user_input)
        conversation.append(human_msg)
        
        # Generate AI response using the LLM model
        ai_response = LLM_Model(conversation)
        messages.append(f"Bot: {ai_response.content}")
        conversation.append(CreateAIMessage(ai_response.content))
        print("*******************************")
        print(messages)
        print("------------------------------")


    return jsonify(messages=messages)

@app.route('/clear', methods=['POST'])
def clear():
    global conversation, messages
    conversation = []
    messages = []
    # Reset the system message
    system_msg = CreateSystemMessage(text=All_QuestionsWithAllDataWithoutCommentsNewTemplte)
    conversation.append(system_msg)
    return jsonify(messages=[])

if __name__ == "__main__":
    app.run(debug=True)


