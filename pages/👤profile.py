# display contents of the profile page
import streamlit as st
import time

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
    # Button to return to home
    if st.button("🏡Back to Home"):
        st.switch_page("home.py")

    if 'user_profile' in st.session_state:
        profile = st.session_state.user_profile

    if 'user_profile' in st.session_state:
        st.title(f"👤 {profile.get('name')}")
    
    # Display user profile information
        st.write(f"**Name:** {profile.get('name', 'N/A')}")
        st.write(f"**Familiar Subjects:** {', '.join(profile.get('familiar_subjects', [])) if profile.get('familiar_subjects') else 'N/A'}")
        st.write(f"**Knowledge Level:** {profile.get('experience', 'N/A')}")
        st.write(f"**Description of Knowledge:** {profile.get('goals', 'N/A')}")

        st.info('''💡
            The above recorded information of your knowledge is just an easy and quick way to estimate your knowledge level. It is generally
            sufficient for us to start providing you with good enough personalized highlights and improve as you use our system. To have a more
            accurate personalized experience, we recommend you to take some quizzes we've prepared to assess your knowledge level.
                 ''')
        if st.button("🧠Test Knowledge"):
            st.switch_page("🧠test_knowledge.py")

        st.subheader("Your Knowledge Map")
        st.write("Visualization of your current knowledge based on papers you've read and your manual inputs of knowledge level. (Imagine this map is interactive and each node is clickable to show more details.🙂)")
        st.image("media/images/knowledge-map.png", caption="Knowledge Map")
    else:
        st.title("👤 Profile")
        st.write("No profile information available. Please set up your profile first.")
        if st.button("Set up Profile"):
            initial_setup()

if __name__ == "__main__":
    main()