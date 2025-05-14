import streamlit as st
import time

def bot_response_generator(user_input):
    """Generate streaming bot responses based on user input"""
    if "paper" in user_input.lower():
        response = "You can upload a paper using the 'Upload Paper' button. I can help you understand it better!"
    elif "quiz" in user_input.lower() or "test" in user_input.lower():
        response = "Click on the 'Test Knowledge' button to take quizzes on papers you've read or explore your knowledge map."
    elif "mode" in user_input.lower() or "reading" in user_input.lower():
        response = "We offer three reading modes: Exploratory (for new ideas), Understanding (for comprehensive learning), and Revisiting (for quick review)."
    else:
        response = "How can I help you with your academic paper reading experience today? You can ask about reading modes, paper uploads, or knowledge testing."
    
    # Stream the response word by word
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def main():
    # Initialize chat history in session state if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar chat interface
    with st.sidebar:
        st.title("Paper Reading Assistant")
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("What is up?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(bot_response_generator(prompt))
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})        

    # Main content
    _, col1, _ = st.columns(3)
    with col1:
        st.image("media/images/idea.png")
    
    st.markdown("<h2 style='text-align: center;'>Smart Paper Reader</h2>", unsafe_allow_html=True)
    st.markdown('''
        Welcome to **Smart Paper Reader**, an intelligent tool that helps you read and understand academic papers
        based on your knowledge level and learning goals.
                
        The system adapts content presentation based on your reading mode and helps you test your knowledge.
    ''')

    # Main navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Read Paper", use_container_width=True):
            # Navigate to the upload paper page
            st.switch_page("pages/read_paper.py")
    
    with col2:
        if st.button("🧠 Test Knowledge", use_container_width=True):
            # Navigate to the test knowledge page
            st.switch_page("pages/test_knowledge.py")

if __name__=="__main__":
    st.set_page_config(page_title="Smart Paper Reader", page_icon="media/images/idea.png")
    main()