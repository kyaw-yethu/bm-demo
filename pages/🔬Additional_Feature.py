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
    
    # Create tabs for different features
    feature_tabs = st.tabs(["Paper Recommendations", "Knowledge Analytics", "Collaboration", "Study Planner", "Citation Manager"])
    
    # Paper Recommendations tab
    with feature_tabs[0]:
        st.header("📚 Paper Recommendations")
        st.write("Discover papers tailored to your knowledge level and interests.")
        
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
        st.subheader("Your Personalized Recommendations")
        
        for i in range(3):
            with st.expander(f"Paper {i+1}: AI Business Integration Strategies {2023-i}"):
                st.write(f"**Authors**: J. Smith, A. Johnson, et al.")
                st.write(f"**Abstract**: This paper examines how businesses can effectively integrate AI solutions...")
                st.write(f"**Topics**: AI in Business, Decision-Making")
                st.write(f"**Difficulty**: {'Intermediate' if i==0 else 'Advanced' if i==1 else 'Beginner'}")
                st.write(f"**Est. Reading Time**: {20+i*5} minutes")
                
                col1, col2 = st.columns([1,1])
                with col1:
                    if st.button(f"Read Now {i+1}", key=f"read_now_{i}"):
                        st.switch_page("pages/📄Read_Paper.py")
                with col2:
                    st.button(f"Save for Later {i+1}", key=f"save_{i}")
    
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
    
    # Study Planner tab
    with feature_tabs[3]:
        st.header("📅 Study Planner")
        st.write("Create and manage your academic reading schedule.")
        
        # Calendar view
        st.subheader("Your Reading Calendar")
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        days = [(start_of_week + timedelta(days=i)).strftime("%a %m/%d") for i in range(7)]
        
        # Display week calendar
        st.write("This Week:")
        cols = st.columns(7)
        for i, day in enumerate(days):
            with cols[i]:
                st.write(f"**{day}**")
                if i == 2:
                    st.info("2 papers")
                elif i == 4:
                    st.info("1 paper")
                else:
                    st.write("—")
        
        # Plan new reading session
        st.divider()
        st.subheader("Plan a Reading Session")
        
        col1, col2 = st.columns(2)
        with col1:
            st.date_input("Date", value=today)
            st.time_input("Start Time", value=datetime.strptime("14:00", "%H:%M"))
            st.time_input("End Time", value=datetime.strptime("15:30", "%H:%M"))
            
        with col2:
            st.selectbox("Paper to Read", ["Select a paper...", "Smith et al. - AI Integration", 
                                          "Johnson - Business Models", "Williams & Brown - Ethics"])
            st.selectbox("Reading Mode", ["Exploratory", "Understanding", "Revisiting"])
            st.text_area("Session Goals", placeholder="What do you want to learn from this session?")
        
        if st.button("Schedule Session"):
            st.success("Reading session scheduled successfully!")
    
    # Citation Manager tab
    with feature_tabs[4]:
        st.header("📝 Citation Manager")
        st.write("Organize citations from papers you've read.")
        
        # Search and filter
        st.text_input("Search citations", placeholder="Search by author, title, or keyword...")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.selectbox("Sort by", ["Date Added", "Author", "Title", "Publication Year"])
        with col2:
            st.multiselect("Filter by topic", ["AI & Labor", "Human-AI Interaction", "Data Economy"])
        with col3:
            st.selectbox("Export format", ["BibTeX", "EndNote", "RIS", "APA", "MLA"])
            
        # Sample citations
        citations = [
            {
                "title": "AI Integration Frameworks for Modern Business",
                "authors": "Smith, J., Johnson, A., & Davis, M.",
                "journal": "Journal of Business Technology",
                "year": "2023",
                "doi": "10.1234/jbt.2023.1234"
            },
            {
                "title": "Ethical Considerations in AI Implementation",
                "authors": "Williams, R. & Brown, T.",
                "journal": "AI Ethics Quarterly",
                "year": "2023",
                "doi": "10.5678/aeq.2023.5678"
            },
            {
                "title": "Business Models for AI-Driven Companies",
                "authors": "Johnson, P.",
                "journal": "Strategic Management Review",
                "year": "2022",
                "doi": "10.9101/smr.2022.9101"
            }
        ]
        
        for i, citation in enumerate(citations):
            with st.expander(f"{citation['authors']} ({citation['year']}) - {citation['title']}"):
                st.write(f"**Title:** {citation['title']}")
                st.write(f"**Authors:** {citation['authors']}")
                st.write(f"**Journal:** {citation['journal']}")
                st.write(f"**Year:** {citation['year']}")
                st.write(f"**DOI:** {citation['doi']}")
                
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    st.button(f"Copy Citation {i}", key=f"copy_{i}")
                with col2:
                    st.button(f"Edit {i}", key=f"edit_{i}")
                with col3:
                    st.button(f"Delete {i}", key=f"delete_{i}")
        
        # Export function
        st.divider()
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("Export all citations or selected citations to use in your own work.")
        with col2:
            if st.button("Export Citations"):
                st.success("Citations exported successfully!")

if __name__ == "__main__":
    main()
