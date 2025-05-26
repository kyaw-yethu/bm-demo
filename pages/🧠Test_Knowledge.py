import streamlit as st
import time


def main():
    # Button to return to home
    if st.button("🏡Back to Home"):
        st.switch_page("Home.py")

    st.title("🧠Test Your Knowledge")
    
    # st.subheader("Test Your Understanding")
    st.write("Take a quiz to test your knowledge on a certain AI-business topic. Your knowledge will be updated reflecting the quiz result. The quizzes are created based on this [dataset of papers](https://docs.google.com/spreadsheets/d/1b5a3bLdPOY6ulVE-cds4q8znyLGSp3OPg7yphZc6s9I/edit?usp=sharing).")
    options = ["AI & Labor", "Human-AI Interaction", "Data & Data Economy", "AI in Business/Management",
         "AI & Decision-Making", "AI in Healthcare", "Automation & Tech Evolution", 
         "AI History & Trends", "AI & Society"]
    
    selection = st.pills("Topics", options, selection_mode="single")
    
    
    # Display quiz after generation
    if selection:            
        st.subheader(f"Quiz for {selection}")
        
        # Sample quiz questions
        questions = [
            {
                "question": "Which of the following best describes how AI can create competitive advantage in business?",
                "options": [
                    "By replacing all human workers",
                    "By creating new products and services through analyzing data patterns",
                    "By automating all decision-making processes",
                    "By increasing operational costs"
                ],
                "correct": 1
            },
            {
                "question": "What is a key challenge of implementing AI in traditional organizations?",
                "options": [
                    "Technical limitations of current AI systems",
                    "Resistance to change and cultural barriers",
                    "High hardware costs",
                    "Lack of use cases"
                ],
                "correct": 1
            },
            {
                "question": "How does organizational structure typically need to change when adopting AI?",
                "options": [
                    "No change is necessary",
                    "More hierarchical structures are needed",
                    "Cross-functional teams and flatter hierarchies become more important",
                    "Complete centralization of all decisions"
                ],
                "correct": 2
            }
        ]
        
        # Display questions with radio buttons
        user_answers = {}
        for i, q in enumerate(questions):
            st.write(f"**Question {i+1}:** {q['question']}")
            answer = st.radio(
                f"Select one.",
                q['options'],
                key=f"q{i}"
            )
            user_answers[i] = q['options'].index(answer)
            st.write("---")
        
        # Submit button
        if st.button("Submit Answers"):
            correct_count = sum(1 for q_idx, ans_idx in user_answers.items() 
                                if ans_idx == questions[q_idx]['correct'])
            wrong_questions = [i for i, ans in user_answers.items() if ans != questions[i]['correct']]
            
            st.success(f"You got {correct_count} out of {len(questions)} correct! ")
            # suggest for improvements based on the submitted answers
            for wrong_question in wrong_questions:
                st.info(f'''
                            Question {wrong_question + 1}. 
                            Your answer: {questions[wrong_question]['options'][user_answers[wrong_question]]} |
                        Correct answer: {questions[wrong_question]['options'][questions[wrong_question]['correct']]} \n
                        Please read the following papers to see why:
                    ''')

    # with knowledge_tabs[2]:
    #     st.subheader("Recommended Papers")
    #     st.write("Based on your reading history, we suggest these papers:")
    #     for i in range(3):
    #         with st.expander(f"Paper {i+1}: Advanced Topic in Area {i+1}"):
    #             st.write(f"This paper builds on concepts you've already mastered and introduces new ideas in area {i+1}.")
    #             if st.button(f"Read Paper {i+1}", key=f"read_{i}"):
    #                 st.switch_page("pages/upload_paper.py")

if __name__ == "__main__":
    main()