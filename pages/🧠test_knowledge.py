import streamlit as st
import time


def main():
    # Button to return to home
    if st.button("🏡Back to Home"):
        st.switch_page("home.py")

    st.title("🧠Test Your Knowledge")
    
    # Create tabs for the test knowledge section
    knowledge_tabs = st.tabs(["Input Your Knowledge", "Quiz Your Knowledge", "Knowledge Map", "Paper Suggestions"])
    
    # **Input Your Knowledge** tab
    with knowledge_tabs[0]:
        st.subheader("Input Your Knowledge")
        st.markdown('''
                 Please tell us about how much you already understand AI-business by taking a relevant test below.
                This will help us to adapt the content presentation to your knowledge level. See [the papers](https://docs.google.com/spreadsheets/d/1b5a3bLdPOY6ulVE-cds4q8znyLGSp3OPg7yphZc6s9I/edit?usp=sharing) 
                we based our tests on.
        ''')
        options = ["Beginner", "Intermediate", "Advanced"]
        selection = st.segmented_control(
            "Level", options, selection_mode="single"
        )
        if selection == "Novice":
            st.subheader("Test for novices.")
            
            # Novice level quiz
            st.write("Please answer these basic questions about AI in business:")
            
            q1 = st.radio(
                "What does AI stand for?",
                ["Automated Intelligence", "Artificial Intelligence", "Augmented Innovation", "Advanced Integration"],
                key="novice_q1"
            )
            
            q2 = st.radio(
                "Which of the following is an example of AI in business?",
                ["Using Excel for calculations", "Installing antivirus software", 
                 "Chatbots for customer service", "Creating PowerPoint presentations"],
                key="novice_q2"
            )
            
            q3 = st.radio(
                "What is a primary benefit of AI for businesses?",
                ["Replacing all employees", "Automating repetitive tasks", 
                 "Eliminating the need for management", "Making business more complicated"],
                key="novice_q3"
            )
            
            if st.button("Submit Answers", key="novice_check"):
                score = 0
                if q1 == "Artificial Intelligence": score += 1
                if q2 == "Chatbots for customer service": score += 1
                if q3 == "Automating repetitive tasks": score += 1
                
                st.success(f'''You scored {score} out of 3! We've recorded your level of knowledge. 
                           Please check 'Knowledge Map' section to visualize how we've initialized your knowledge.''')
            
        elif selection == "Undergrad Level":
            st.subheader("Test for undergraduates.")
            
            # Undergrad level quiz
            st.write("Please answer these intermediate questions about AI in business:")
            
            q1 = st.radio(
                "Which of these is NOT a common machine learning approach?",
                ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Obligatory Learning"],
                key="undergrad_q1"
            )
            
            q2 = st.radio(
                "What is a key challenge when implementing AI in existing business processes?",
                ["Data quality and availability", "Hardware costs", 
                 "Programming language selection", "Office space requirements"],
                key="undergrad_q2"
            )
            
            q3 = st.radio(
                "Which business function has seen the LEAST AI adoption to date?",
                ["Customer service", "Marketing", "Supply chain management", "Legal and compliance"],
                key="undergrad_q3"
            )
            
            if st.button("Submit Answers", key="undergrad_check"):
                score = 0
                if q1 == "Obligatory Learning": score += 1
                if q2 == "Data quality and availability": score += 1
                if q3 == "Legal and compliance": score += 1
                
                st.success(f'''You scored {score} out of 3! We've recorded your level of knowledge. 
                           Please check 'Knowledge Map' section to visualize how we've initialized your knowledge.''')
            
        elif selection == "Graduate Level":
            st.subheader("Test for graduates.")
            
            # Graduate level quiz
            st.write("Please answer these advanced questions about AI in business:")
            
            q1 = st.radio(
                "Which approach best describes the concept of 'AI alignment' in business?",
                ["Ensuring AI systems operate according to human intentions and values", 
                 "Aligning AI development with quarterly business goals",
                 "Matching AI capabilities to hardware specifications", 
                 "Synchronizing AI outputs with marketing campaigns"],
                key="grad_q1"
            )
            
            q2 = st.radio(
                "What is the transformer architecture primarily known for in business applications?",
                ["Powering electrical systems more efficiently", 
                 "Processing natural language for applications like chatbots and content generation",
                 "Transforming raw materials in manufacturing", 
                 "Converting business metrics into graphical representations"],
                key="grad_q2"
            )
            
            q3 = st.radio(
                "Which concept describes the challenge of explaining how AI systems reach their conclusions?",
                ["The black box problem", "The transparency paradox", 
                 "The interpretability dilemma", "The explainability gap"],
                key="grad_q3"
            )
            
            if st.button("Submit Answers", key="grad_check"):
                score = 0
                if q1 == "Ensuring AI systems operate according to human intentions and values": score += 1
                if q2 == "Processing natural language for applications like chatbots and content generation": score += 1
                if q3 == "The black box problem": score += 1
                
                st.success(f'''You scored {score} out of 3! We've recorded your level of knowledge. 
                           Please check 'Knowledge Map' section to visualize how we've initialized your knowledge.''')
                
    
    # **Quiz Your Knowledge** tab
    with knowledge_tabs[1]:
        st.subheader("Test Your Understanding")
        st.write("Take a quiz to test your knowledge on papers you've read.")
        options = ["AI", "Business", "Organizational Management", "Finance"]
        selection = st.pills("Topics", options, selection_mode="multi")
        selection = ', '.join(selection)
        
        # Initialize quiz state in session state
        if 'quiz_generated' not in st.session_state:
            st.session_state.quiz_generated = False
        if 'quiz_topics' not in st.session_state:
            st.session_state.quiz_topics = ""
        
        # Generate quiz button with loading and quiz display
        if st.button("Generate Quiz", key="generate-quiz"):
            with st.spinner("Generating your personalized quiz..."):
                # Simulate loading delay
                time.sleep(3)
                st.session_state.quiz_generated = True
                st.session_state.quiz_topics = selection
                st.rerun()
        
        # Display quiz after generation
        if st.session_state.quiz_generated:
            topics = st.session_state.quiz_topics if st.session_state.quiz_topics else "selected topics"
            st.success(f"Quiz generated for: {topics}")
            
            st.subheader("Quiz Questions")
            
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
                
                st.success(f"You got {correct_count} out of {len(questions)} correct!")
                # suggest for improvements based on the submitted answers
                for wrong_question in wrong_questions:
                    st.info(f'''
                             Question {wrong_question + 1}. 
                             Your answer: {questions[wrong_question]['options'][user_answers[wrong_question]]} |
                            Correct answer: {questions[wrong_question]['options'][questions[wrong_question]['correct']]} \n
                            Please read the following papers to see why:
                        ''')

    
    with knowledge_tabs[2]:
        st.subheader("Your Knowledge Map")
        st.write("Visualization of your current knowledge based on papers you've read.")
        st.image("media/images/knowledge-map.png", caption="Knowledge Map")

    with knowledge_tabs[3]:
        st.subheader("Recommended Papers")
        st.write("Based on your reading history, we suggest these papers:")
        for i in range(3):
            with st.expander(f"Paper {i+1}: Advanced Topic in Area {i+1}"):
                st.write(f"This paper builds on concepts you've already mastered and introduces new ideas in area {i+1}.")
                if st.button(f"Read Paper {i+1}", key=f"read_{i}"):
                    st.switch_page("pages/upload_paper.py")

if __name__ == "__main__":
    main()