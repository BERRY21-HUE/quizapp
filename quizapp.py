import streamlit as st

questions = ["Which language has the more native speakers: ",
             "How many minutes are in a full week: ",
             "Which planet in the Milky Way is the hottest: ",
             "What city is known as 'The Eternal City': ",
             "Which planet has the most moons: ",
             "Kratos is the main character of what video game series: ",
             "How many bones do we have in an ear: ",
             "What year did Nigeria gain Independence: ",
             "When was the movie the Titanic released: ",
             "How many times has England won the men's football World Cup: ",
             "Who was the first human to travel into space: ",
             "Which animal has a fingerprint extremely similar to a human being: ",
             "What does Hakuna Matata mean: ",
             "Which planet is closest to the sun: ",
             "How many days are in a leap year: "
    ]

options = [("A. English","B. Yoruba","C. Spanish","D. Chinese"),
           ("A. 365","B. 1080","C. 900","D. 1112"),
           ("A. Earth","B. Jupiter","C. Mars","D. Venus"),
           ("A. Toledo","B. New York City","C. Rome","D. Tokyo"),
           ("A. Saturn", "B. Venus", "C. Mecury", "D. Earth"),
           ("A. Assasin's Creed","B. Devil May Cry","C. God Of War","D. Star wars"),
           ("A. 3","B. 6","C. 1","D. 0"),
           ("A. 1885","B. 1960","C. 1965","D. 1980"),
           ("A. 1960","B. 1997","C. 1871","D. 2001"),
           ("A. Twice","B. Never","C. Once","D. Thrice"),
           ("A. George Washington","B. Michael Faraday","C. Yuri Gagarin","D. Thomas Edison"),
           ("A. Monkey","B. Koala","C. Penguin","D. Ape"),
           ("A. Goodluck","B. Lets Party","C. Have a nice day","D. No worries"),
           ("A. Earth","B. Mecury","C. Saturn","D. Venus"),
           ("A. 360","B. 366","C. 365","D. 368")
]

answers = ["C", "B", "D", "C", "A", "C", "A", "B", "B", "C", "C", "B", "D", "B", "B"]

question_num = 0
score = 0
guesses = []

if "user_guess" not in st.session_state:
    st.session_state.user_guess = [""] * len(questions)

st.title("BASIC QUIZ")
user_name = st.text_input("Enter Your Name", placeholder="John")
if user_name:
    for i, question in enumerate(questions):
        st.info(f"Question {i + 1}: {question}")
        for option in options[question_num]:
            st.write(option)

        st.session_state.user_guess[i] = st.text_input(
            f"Your Answer for Question{i + 1}".upper(),
            value=st.session_state.user_guess[i],
            key=f"user_{i}")

        guesses.append(st.session_state.user_guess[i])
        if st.session_state.user_guess[i].strip().upper() == answers[question_num].strip().upper():
            score += 1
        question_num += 1

    if st.button("SUBMIT"):
        st.info(f"Your Answers: {guesses}")
        st.info(f"The Answers: {answers}")
        overall_score = (score / len(questions)) * 100
        st.write(f"{user_name}, Your Score is {overall_score:.1f}%")

