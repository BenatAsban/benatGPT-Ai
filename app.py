# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

import openai
import streamlit as st

openai.api_key = "your-api-key"


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message benatGPT"):
    
    
 def generate_response(prompt):
    if "." in prompt.lower():
        return "1. name\n2. hi\n3. how are you\n4. fine\n5. yes\n6. saptiya\n7. who made you?\n8. hlo\n9. what is python?\n10. what is streamlit?\n11. bye\n12. thank you"
    elif "name" in prompt.lower():
        return "I am ChatGPT."
    elif "hi" in prompt:
        return "hello,Have a nice day."
    elif "how are you" in prompt:
        return "Thank you for asking me.I am GREAT.How about you?"
    elif "fine" in prompt:
        return "Great to hear! Is there anything else you need assistance with me?"
    elif "yes" in prompt:
        return "Ask me your question and i will answer you"
    elif "saptiya" in prompt.lower():
        return "Arivu illaya unaku na roboot.na sapudamaten"
    elif "who made you?" in prompt.lower():
        return "Mr.benat created me"
    elif "hlo" in prompt.lower():
        return "Ena na roboot nala,adika maten nu hlo soldriya.un viratha enta kamikura.unaku vekkama illa.thu..."
    elif "what is python?" in prompt.lower():
        return "Python is a high-level, interpreted programming language renowned for its simplicity, readability, and versatility. Developed by Guido van Rossum in the early 1990s, Python emphasizes clean, concise syntax that makes it easy for programmers to write and understand code. Its dynamic typing system allows for flexibility in coding while its multi-paradigm support accommodates various programming styles. Python boasts a rich standard library covering diverse functionalities, from file I/O to web development. Additionally, its extensive ecosystem of third-party libraries and frameworks facilitates tasks such as data analysis, machine learning, and web scraping. Python's cross-platform compatibility further enhances its appeal, making it a go-to choice for developers worldwide."
    elif "what is streamlit?" in prompt.lower():
        return "Streamlit is a Python library for effortlessly creating web applications. It simplifies the process of transforming data scripts into interactive web apps with minimal code. With built-in widgets and seamless integration with data science libraries, Streamlit facilitates rapid prototyping and deployment, making it invaluable for data-driven application development."
    elif "bye" in prompt.lower():
        return "Goodbye!.Have a great day!"
    elif "thank you" in prompt.lower():
        return "You're welcome!.Have a wonderful day!"
    else:
        return "I'm not sure how to respond to that."
    
    
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("User"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = generate_response(prompt)
        message_placeholder = st.empty()
        message_placeholder.markdown(response)
         
    full_response = generate_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": full_response})