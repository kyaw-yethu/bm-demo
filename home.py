import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

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

def main():
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
        # File uploader is directly available
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        
        if uploaded_file is not None:
            reading_mode = st.radio(
                "Select Reading Mode:",
                ["Exploratory", "Understanding", "Revisiting"],
                horizontal=True
            )
            
            st.subheader(f"Reading in {reading_mode} Mode")
            
            # Display different annotation styles based on reading mode
            mode_annotations = annotations.copy()
            if reading_mode == "Exploratory":
                st.info("Only highlighting new key ideas. Well-known sections are auto-collapsed with summaries.")
                mode_annotations[0]["color"] = "blue"
            elif reading_mode == "Understanding":
                st.info("Highlighting key ideas, supporting examples, and contextual setup with varying levels of highlighting.")
                mode_annotations[0]["color"] = "green"
            else:  # Revisiting
                st.info("Skipping parts that set up context for main contents. Showing connections to your new knowledge.")
                mode_annotations[0]["color"] = "orange"
            
            # PDF Viewer with mode-specific annotations
            pdf_viewer(
                input = "media/docs/asst6.pdf",  # Using default PDF, would use uploaded_file in production
                height = 800,
                width = 800,
                render_text = True,
                on_annotation_click=my_custom_annotation_handler,
                annotations=mode_annotations
            )
        else:
            st.info("Upload a paper to start reading with our intelligent interface.")
            
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
            topic = st.selectbox("Select Topic", ["Machine Learning", "Computer Vision", "Natural Language Processing"])
            if st.button("Start Quiz"):
                st.info("Quiz will start with 10 questions about " + topic)
                # Quiz questions would be displayed here

if __name__=="__main__":
    st.set_page_config(page_title="Smart Paper Reader", page_icon='images/logo.png')
    main()
