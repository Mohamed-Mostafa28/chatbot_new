import streamlit as st
from transformers import GPT2Tokenizer  # Use your specific model's tokenizer
from model import LLM_Model  # Custom model, replace with your logic
from Create_Messages import CreateHumanMessage, CreateAIMessage, CreateSystemMessage
# from prompt import All_QuestionsWithAllDataWithoutCommentsNewTemplte
from prompt import get_all_message
from createPersonalInf import get_random_profile

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")  # Replace with your specific tokenizer

# Function to calculate total tokens
# def calculate_total_tokens(conversation):
#     total_tokens = 0
#     for message in conversation:
#         # Check if the message has a content or text attribute
#         if hasattr(message, "content"):
#             tokens = tokenizer.encode(message.content)
#         elif hasattr(message, "text"):
#             tokens = tokenizer.encode(message.text)
#         else:
#             # If the message doesn't have content, skip it
#             print(f"Message has no valid content: {message}")  # Debugging line
#             continue  
#         total_tokens += len(tokens)
#     return total_tokens

# Set up the UI
st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
st.title("Medical Chatbot 🧠")
st.markdown("This chatbot helps doctors by collecting medical data from patients!")


# Initialize session state for conversation and messages
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# if "alltokenssss" not in st.session_state:
#     st.session_state.alltokenssss = 0
    
if "my_info" not in st.session_state:
    st.session_state.my_info = get_random_profile()
    

# Add initial system message if the conversation is empty
if not st.session_state.conversation:
    # system_msg = CreateSystemMessage(text=All_QuestionsWithAllDataWithoutCommentsNewTemplte)
    system_msg = CreateSystemMessage(text=get_all_message(st.session_state.my_info))
    st.session_state.conversation.append(system_msg)

# Display previous messages (user and bot messages)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input through a chat-like interface
if user_input := st.chat_input("Ask a medical question..."):
    # Add user's message to conversation and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    human_msg = CreateHumanMessage(text=user_input)
    st.session_state.conversation.append(human_msg)
    
    # Generate AI response using your custom LLM model
    ai_response = LLM_Model(st.session_state.conversation)  # Use your custom model here
    
    # Display assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ai_response.content  # Assuming your model returns a single response

        message_placeholder.markdown(full_response)  # Display final response
    
    # Add assistant response to the conversation
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.conversation.append(CreateAIMessage(full_response))

# # Calculate total tokens in the conversation
# total_tokens = calculate_total_tokens(st.session_state.conversation)
# st.session_state.alltokenssss+=total_tokens
# st.write(f"Total Tokens in Conversation: {total_tokens}")
# st.write(f"all new and old Tokens in Conversation: {st.session_state.alltokenssss}")
# print("----------------------------------------")
# print(st.session_state.conversation)

# print("=========================================")


# Clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.conversation = []
    # st.session_state.alltokenssss=0
    st.session_state.my_info=get_random_profile()





# import streamlit as st
# # from dotenv import load_dotenv
# from model import LLM_Model  # Custom model, replace with your logic
# from Create_Messages import CreateHumanMessage, CreateAIMessage, CreateSystemMessage
# from prompt import All_QuestionsWithAllDataWithoutCommentsNewTemplte

# # Load environment variables (if necessary)
# # load_dotenv()

# # Set up the UI
# st.set_page_config(page_title="Medical Chatbot", page_icon="🤖")
# st.title("Medical Chatbot 🧠")
# st.markdown("This chatbot helps doctors by collecting medical data from patients!")

# # Initialize session state for conversation and messages
# if "conversation" not in st.session_state:
#     st.session_state.conversation = []
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Add initial system message if the conversation is empty
# if not st.session_state.conversation:
#     system_msg = CreateSystemMessage(text=All_QuestionsWithAllDataWithoutCommentsNewTemplte)
#     st.session_state.conversation.append(system_msg)

# # Display previous messages (user and bot messages)
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Handle user input through a chat-like interface
# if user_input := st.chat_input("Ask a medical question..."):
#     # Add user's message to conversation and display it
#     st.session_state.messages.append({"role": "user", "content": user_input})
    
#     with st.chat_message("user"):
#         st.markdown(user_input)
    
#     human_msg = CreateHumanMessage(text=user_input)
#     st.session_state.conversation.append(human_msg)
    
#     # Generate AI response using your custom LLM model
#     ai_response = LLM_Model(st.session_state.conversation)  # Use your custom model here
    
#     # Display assistant's response
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ai_response.content  # Assuming your model returns a single response

#         message_placeholder.markdown(full_response)  # Display final response
    
#     # Add assistant response to the conversation
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
#     st.session_state.conversation.append(CreateAIMessage(full_response))

# # Clear chat history
# if st.button("Clear Chat"):
#     st.session_state.messages = []
#     st.session_state.conversation = []
