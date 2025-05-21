import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from streamlit_option_menu import option_menu
import time
import json

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

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

def my_custom_annotation_handler(annotation):
    st.toast("Seen✅, Understood🧠, Revisit❓")


def main():
    # Initialize chat history in session state if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Sidebar chat interface
    with st.sidebar:
        st.title("Chat")

        explain = st.button("Explain selected lines")
        prompt = st.chat_input("What is up?")
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


        if explain:
            st.session_state.messages.append({"role": "user", "content": "Explain selected lines"})
            with st.chat_message("user"):
                st.markdown("Explain selected lines")
            with st.chat_message("assistant"):
                response = st.write_stream(bot_response_generator("Explain selected lines"))
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
        # Accept user input
            if prompt:
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


    # Button to return to home
    if st.button("🏡Back to Home"):
        st.switch_page("home.py")

    st.title("📄Read Paper")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:

        # Save the file information to session state
        if 'uploaded_paper' not in st.session_state:
            st.session_state.uploaded_paper = uploaded_file
        
        # Offering to generate a pre-quiz
        st.text("Generate and take a quiz to assess how much you've already known about the paper.")
        if st.button("Generate a pre-quiz", key="generate-pretest"):
            # Navigate to the reading page
            st.info("Some pre-quiz will be generated...")

        options = ["Exploratory", "Understanding", "Revisiting"]
        selection = st.segmented_control(
            "Reading Mode", options, selection_mode="single", default="Understanding"
        )
        if selection == "Exploratory":
            st.text(f"Viewing in {selection} mode")
            with open("annotations/anno1.json", "r") as f:
                annotations = json.load(f)

        elif selection == "Understanding":
            st.text(f"Viewing in {selection} mode")
            with open("annotations/anno2.json", "r") as f:
                annotations = json.load(f)
            
        elif selection == "Revisiting":
            st.text(f"Viewing in {selection} mode")
            with open("annotations/anno3.json", "r") as f:
                annotations = json.load(f)

        # Display the PDF viewer with the uploaded file
        pdf_viewer(
            uploaded_file.read(),
            width=1200,
            height=1000,
            annotations=annotations,
            on_annotation_click=my_custom_annotation_handler,
            # render_text=True,
        )
    else:
        # Display some info about reading modes when no file is uploaded
        with st.expander("Learn about our Reading Modes"):
            st.write("""
                ### Reading Modes
                
                **Exploratory Mode**
                - Only highlights new key ideas
                - Auto-collapses well-known sections with a one-line summary
                - Knowledge base isn't updated
                
                **Understanding Mode**
                - Highlights key ideas, supporting examples, contextual setup
                - Uses different colors for different importance levels
                - Shows how ideas connect to your prior knowledge
                
                **Revisiting Mode**
                - Skips parts that set up context for main contents
                - Shows connections to knowledge you've acquired since first reading
            """)

if __name__ == "__main__":
    main()