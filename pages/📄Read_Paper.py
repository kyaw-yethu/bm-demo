import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import time
import json
import os

def bot_response_generator(user_input):
    """Generate streaming bot responses based on user input"""
    if "explain" in user_input.lower():
        response = "This is a simple explanation for the super complicated lines you selected."
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

@st.dialog("What are reading modes?")
def show_help_reading_mode():
        
    st.markdown("""        
        **Exploratory Mode**
        - Only highlights new key ideas
        - Auto-collapses well-known sections with a one-line summary
        - Knowledge base isn't updated
        
        **Understanding Mode**
        - Highlights key ideas, supporting examples, contextual setup
        - Uses different colors for different importance levels
        - Shows how ideas connect to your prior knowledge
    """)

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
        st.switch_page("Home.py")

    st.title("📄Read Paper")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save the file information to session state
        if 'uploaded_paper' not in st.session_state:
            st.session_state.uploaded_paper = uploaded_file
        
        col_left, col_right = st.columns([0.9, 0.1])
        with col_left:
            options = ["Exploratory", "Understanding"]
            selection = st.segmented_control(
                "Reading Mode", options, selection_mode="single", default="Understanding"
            )
        with col_right:
            if st.button("❓", help="Learn about reading modes"):
                # Set flag to show help dialog
                st.session_state.show_help_dialog = True
                show_help_reading_mode()

        pdf_content = None
        
        if selection == "Exploratory":
            st.text(f"Viewing in {selection} mode")
            # Use the exploratory-mode.pdf file instead of uploaded file
            with open("media/docs/toward-human-centered-algorithm-design-exploratory.pdf", "rb") as f:
                pdf_content = f.read()
            with open("annotations/anno1.json", "r") as f:
                annotations = json.load(f)

        elif selection == "Understanding":
            st.text(f"Viewing in {selection} mode")
            # Use the understanding-mode.pdf file instead of uploaded file
            with open("media/docs/toward-human-centered-algorithm-design-exploratory-understanding.pdf", "rb") as f:
                pdf_content = f.read()
            with open("annotations/anno2.json", "r") as f:
                annotations = json.load(f)
            
        # elif selection == "Revisiting":
        #     st.text(f"Viewing in {selection} mode")
        #     # Continue using the uploaded file for Revisiting mode
        #     with open("media/docs/exploratory-mode.pdf", "rb") as f:
        #         pdf_content = f.read()
        #     with open("annotations/anno3.json", "r") as f:
        #         annotations = json.load(f)

        # Display the PDF viewer with the appropriate content
        pdf_viewer(
            pdf_content,
            width=1200,
            height=1000,
            # annotations=annotations,
            on_annotation_click=my_custom_annotation_handler,
            # render_text=True,
        )
        

if __name__ == "__main__":
    main()