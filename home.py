import streamlit as st
import time

@st.dialog("How Memora works")
def show_help():
    st.subheader("Welcome to Memora!")
    
    st.markdown("""
    ### 📄 Read Paper
    Our main interface where you read academic papers with our intelligent tools. 
    1. **Smart highlighting**: Automatically highlight concepts and ideas in the paper based on your purpose and knowledge level.
    2. **Knowledge Copilot**: Discuss the paper with our AI assistant instantly without inputting any text.
    
    ### 🧠 Test Knowledge
    - Assess your current knowledge level with quizzes
    - Track your learning progress with the Knowledge Map
    - Get paper recommendations based on your interests
    
    ### Tips
    - Use the search function to quickly find content in papers
    - Create annotations while reading to save important points
    - Take quizzes regularly to reinforce your learning
    """)

def main():
    st.logo('media/images/idea.png', icon_image='media/images/idea.png')
    # Help button in the top right corner
    col_left, col_right = st.columns([0.9, 0.1])
    with col_right:
        if st.button("❓", help="Get help"):
            # Set flag to show help dialog
            st.session_state.show_help_dialog = True
            show_help()
    
    
    # Main content
    _, col1, _ = st.columns(3)
    with col1:
        st.image("media/images/idea.png")
    
    st.markdown("<h2 style='text-align: center;'>Memora</h2>", unsafe_allow_html=True)
    st.markdown('''
        Welcome to **Memora**, an intelligent service that helps you read and understand academic papers
        more quickly and efficiently utilizing your knowledge.
                
        **📄 Read Paper**: Upload and read academic paper with our intelligent tools \n
        **🧠 Test Knowledge**: Take quizzes on papers you've read or explore your knowledge map
    ''')

    # Main navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Read Paper", use_container_width=True):
            # Navigate to the upload paper page
            st.switch_page("pages/📄read_paper.py")
    
    with col2:
        if st.button("🧠 Test Knowledge", use_container_width=True):
            # Navigate to the test knowledge page
            st.switch_page("pages/🧠test_knowledge.py")

if __name__=="__main__":
    st.set_page_config(page_title="Memora", page_icon="media/images/idea.png")
    main()