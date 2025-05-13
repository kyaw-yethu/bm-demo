import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import time

annotations = [
    {
        "page": 1,
        "x": 220,
        "y": 255,
        "height": 22,
        "width": 65,
        "color": "green",
        "border": "dotted"
    }
]


def my_custom_annotation_handler(annotation):
    print(f"Annotation {annotation} clicked.")

# Streamed response generator
def bot_response_generator(user_input):
    """Generate streaming bot responses based on user input"""
    if "paper" in user_input.lower():
        response = "You can upload a paper using the file uploader in the 'Upload Paper' tab. I can help you understand it better!"
    elif "quiz" in user_input.lower() or "test" in user_input.lower():
        response = "Head over to the 'Test Knowledge' tab to take quizzes on papers you've read or explore your knowledge map."
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
        
        st.info("🔗 test.pdf line 23-50 selected.")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

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

    # Create tabs for main navigation
    paper_tab, test_tab = st.tabs(["📄 Upload Paper", "🧠 Test Knowledge"])
    
    # Upload Paper section - now in a tab
    with paper_tab:
        placeholder = st.empty()
        placeholder.info("Upload a paper to start reading with our intelligent interface.")

        # File uploader is directly available
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        
        if uploaded_file is not None:
            # remove the placeholder
            placeholder.empty()
            st.text("Generate and take a quiz to assess how much you've already known about the paper.")
            st.button("Generate a pre-quiz", key="generate-pretest.")

            reading_mode = st.segmented_control(
                "Select Reading Mode:",
                ["Exploratory", "Understanding", "Revisiting"],
                selection_mode="single",
            )
            
            st.subheader(f"Reading in {reading_mode} Mode")
            
            # Display different annotation styles based on reading mode
            mode_annotations = annotations.copy()
            
            # Convert the uploaded file to bytes
            pdf_bytes = uploaded_file.read()
            # PDF Viewer with mode-specific annotations
            pdf_viewer(
                input = pdf_bytes,
                height = 800,
                width = 1000,
                render_text = True,
                on_annotation_click=my_custom_annotation_handler,
                annotations=mode_annotations
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
    
    # Test Knowledge section - now in a tab
    with test_tab:
        knowledge_tabs = st.tabs(["Memory Map", "Paper Suggestions", "Quiz Section"])
        
        with knowledge_tabs[0]:
            st.subheader("Your Knowledge Map")
            st.write("Visualization of your current knowledge based on papers you've read.")
            st.image("https://via.placeholder.com/800x400.png?text=Knowledge+Map+Visualization")
            
        with knowledge_tabs[1]:
            st.subheader("Recommended Papers")
            st.write("Based on your reading history, we suggest these papers:")
            for i in range(3):
                with st.expander(f"Paper {i+1}: Advanced Topic in Area {i+1}"):
                    st.write(f"This paper builds on concepts you've already mastered and introduces new ideas in area {i+1}.")
                    st.button(f"Read Paper {i+1}", key=f"read_{i}")
        
        with knowledge_tabs[2]:
            st.subheader("Test Your Understanding")
            st.write("Take a quiz to test your knowledge on papers you've read.")
            options = ["AI", "Business", "Orgnaizational Management", "Finance"]
            selection = st.pills("Directions", options, selection_mode="multi")
            # convert list into string
            selection = ', '.join(selection)
            if st.button("Generate Quiz", key="generate-quiz"):
                st.info("Quiz will start with 10 questions about " + selection)
                # Quiz questions would be displayed here

if __name__=="__main__":
    st.set_page_config(page_title="Smart Paper Reader", page_icon='images/logo.png')
    main()
