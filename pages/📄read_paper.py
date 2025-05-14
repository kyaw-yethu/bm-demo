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

def main():
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
        
        # Display the PDF viewer with the uploaded file
        pdf_viewer(
            uploaded_file.read(),
            width=1200,
            height=1000,
            annotations=annotations,
            on_annotation_click=my_custom_annotation_handler,
            render_text=True,
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