import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def main():
    # Button to return to home
    if st.button("🏡Back to Home"):
        st.switch_page("home.py")

    st.title("🔬 Additional Features")
    st.write("PS: Please be aware that these are not our main features, but ones requested by customers🙂.")
    # Create tabs for different features
    feature_tabs = st.tabs(["Paper Recommendations", "Knowledge Analytics", "Collaboration"])
    
    # Paper Recommendations tab
    with feature_tabs[0]:
        st.header("📚 Paper Recommendations")
        
        st.subheader("Recommendations based on your Knowledge Map")
        for i in range(3):
            with st.expander(f"Paper {i+1}: AI Business Integration Strategies {2023-i}"):
                st.write(f"**Authors**: J. Smith, A. Johnson, et al.")
                st.write(f"**Abstract**: This paper examines how businesses can effectively integrate AI solutions...")
                st.write(f"**Topics**: AI in Business, Decision-Making")
                
                col1, col2 = st.columns([1,1])
                with col1:
                    if st.button(f"Read Now", key=f"read_now_{i}"):
                        st.switch_page("pages/📄read_paper.py")
                with col2:
                    st.button(f"Save for Later", key=f"save_{i}")

        st.subheader("Generate Specific Recommendations")
        col1, col2 = st.columns([2, 1])
        with col1:
            interests = st.multiselect(
                "Filter by topics",
                ["AI & Labor", "Human-AI Interaction", "Data & Data Economy", 
                 "AI in Business/Management", "AI & Decision-Making", "AI in Healthcare"]
            )
            
            difficulty = st.select_slider(
                "Knowledge level",
                options=["Beginner", "Intermediate", "Advanced", "Expert"],
                value="Intermediate"
            )
        
        with col2:
            st.write("Sort by:")
            sort_option = st.radio(
                "",
                ["Relevance", "Publication Date", "Citation Count", "Reading Time"]
            )
        if st.button("Generate Recommendations"):
            with st.spinner("Finding the perfect papers for you..."):
                time.sleep(1.5)
                
        # Sample recommendations

    
    # Knowledge Analytics tab
    with feature_tabs[1]:
        st.header("📊 Knowledge Analytics")
        st.write("Visualize your learning progress and knowledge acquisition over time.")
        
        # Sample visualization data
        reading_dates = pd.date_range(start='1/1/2023', periods=10, freq='W')
        papers_read = np.cumsum(np.random.randint(1, 3, size=10))
        knowledge_score = [40 + i*5 + np.random.randint(-3, 5) for i in range(10)]
        
        # Create tabs for different analytics views
        analytics_tabs = st.tabs(["Reading Activity", "Knowledge Growth", "Topic Coverage"])
        
        with analytics_tabs[0]:
            st.subheader("Your Reading Activity")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(reading_dates, papers_read, marker='o')
            ax.set_xlabel('Date')
            ax.set_ylabel('Cumulative Papers Read')
            ax.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
            
            st.metric("Papers Read This Month", "4", "+2 from last month")
            st.metric("Average Reading Time", "35 minutes", "-5 minutes from average")
            
        with analytics_tabs[1]:
            st.subheader("Knowledge Growth Over Time")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(reading_dates, knowledge_score, marker='o', color='green')
            ax.set_xlabel('Date')
            ax.set_ylabel('Knowledge Score')
            ax.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
            
            st.metric("Overall Knowledge Score", "87/100", "+12 from initial assessment")
            
        with analytics_tabs[2]:
            st.subheader("Topic Coverage")
            topics = ['AI & Labor', 'Human-AI Interaction', 'Data Economy', 
                     'Business/Management', 'Decision-Making', 'Healthcare']
            coverage = [85, 70, 45, 90, 60, 30]
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(topics, coverage, color='skyblue')
            ax.set_xlabel('Knowledge Coverage (%)')
            ax.set_title('Your Topic Mastery')
            ax.grid(True, axis='x', linestyle='--', alpha=0.7)
            st.pyplot(fig)
    
    # Collaboration tab
    with feature_tabs[2]:
        st.header("👥 Collaboration")
        st.write("Share papers and insights with colleagues and collaborators.")
        
        st.subheader("Create or Join a Reading Group")
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Group Name", placeholder="AI Business Strategy Group")
            st.text_area("Group Description", placeholder="A group focused on discussing the latest AI strategies for business...")
            st.selectbox("Privacy", ["Public", "Private (Invitation Only)"])
            st.button("Create Group")
            
        with col2:
            st.subheader("Join Existing Groups")
            groups = ["AI Ethics Discussion", "Future of Work", "ML for Business"]
            for group in groups:
                st.button(f"Join {group}", key=f"join_{group}")
        
        st.divider()
        st.subheader("Share Your Annotations")
        
        paper_to_share = st.selectbox(
            "Select a paper to share your annotations",
            ["Smith et al. (2023) - AI Integration Frameworks", 
             "Johnson (2022) - Business Models for AI", 
             "Williams & Brown (2023) - Ethical Considerations"]
        )
        
        share_with = st.multiselect(
            "Share with",
            ["Alice Johnson", "Bob Smith", "Charlie Brown", "AI Business Strategy Group"]
        )
        
        include_options = st.multiselect(
            "Include",
            ["My highlights", "My notes", "Quiz results", "Knowledge map impact"]
        )
        
        if st.button("Share"):
            st.success("Successfully shared with selected recipients!")
    

if __name__ == "__main__":
    main()
