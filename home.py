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

@st.dialog("Welcome to Memora💡")
def initial_setup():    
    st.write("Please spare just 5~10 minutes to describe the level of your knowledge so that we can better personalize your experience.")
    # Basic information
    name = st.text_input("Your name")
    
    # Research interests (multi-select)
    known_subjects = st.multiselect(
        "Select the AI-business topics that you are familiar with.",
        ["AI & Labor", "Human-AI Interaction", "Data & Data Economy", "AI in Business/Management",
         "AI & Decision-Making", "AI in Healthcare", "Automation & Tech Evolution", 
         "AI History & Trends", "AI & Society"],
        max_selections=10,
    )
    # Reading experience
    experience = st.select_slider(
        "How experienced are you with the topics selected above?",
        options=["Beginner", "Intermediate", "Advanced", "Expert"],
        value="Intermediate"
    )
    
    expertise_description = st.text_area("Can you tell us about your expertise in AI-business? The more specific, the better we can help you.", 
                                 max_chars=300)
    
    # Submit button
    if st.button("Get Started"):
        # Save all preferences to session state
        st.session_state.user_profile = {
            "name": name,
            "familiar_subjects": known_subjects,
            "experience": experience,
            "goals": expertise_description
        }
        
        # Display confirmation
        st.success("Thanks for signing up! Your information have been saved.")
        
        # Give user time to see the success message before rerunning
        time.sleep(1.5)
        st.rerun()
    

def main():
    # Check if this is the first visit
    if 'has_visited_home' not in st.session_state:
        st.session_state.has_visited_home = False

    # Only show the vote dialog on first visit
    if not st.session_state.has_visited_home:
        initial_setup()
        st.session_state.has_visited_home = True
    
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
                
        **📄 Read Paper**: Upload and read academic paper with our intelligent tools (Main Service)\n
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