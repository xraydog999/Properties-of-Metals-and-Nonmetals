import streamlit as st
from PIL import Image

st.title("Main Group Elements & Physical Properties Quiz")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    # Group Identification
    {"q": "Which group contains the alkali metals?", "options": ["Group 1A", "Group 2A", "Group 7A"], "answer": "Group 1A"},
    {"q": "Which group contains the alkaline earth metals?", "options": ["Group 2A", "Group 3A", "Group 8A"], "answer": "Group 2A"},
    {"q": "Which group contains the halogens?", "options": ["Group 6A", "Group 7A", "Group 8A"], "answer": "Group 7A"},
    {"q": "Which group contains the inert gases?", "options": ["Group 8A", "Group 1A", "Group 7A"], "answer": "Group 8A"},

    # Ion Formation
    {"q": "What charge do alkali metals form?", "options": ["1+", "2+", "1−"], "answer": "1+"},
    {"q": "What charge do alkaline earth metals form?", "options": ["1+", "2+", "3+"], "answer": "2+"},
    {"q": "What charge do halogens form?", "options": ["1−", "2−", "0"], "answer": "1−"},
    {"q": "What charge do noble gases typically form?", "options": ["0", "1+", "1−"], "answer": "0"},
    {"q": "Which element is in Group 1A but not a metal?", "options": ["Hydrogen", "Helium", "Carbon"], "answer": "Hydrogen"},
    {"q": "Which group is known for being very reactive?", "options": ["Alkali metals", "Noble gases", "Halogens"], "answer": "Alkali metals"},

    # Physical Properties of Metals
    {"q": "Which is a physical property of metals?", "options": ["Dull", "Brittle", "Luster"], "answer": "Luster"},
    {"q": "Which property allows metals to be drawn into wire?", "options": ["Malleability", "Ductility", "Conductivity"], "answer": "Ductility"},
    {"q": "Which property allows metals to be hammered into shape?", "options": ["Malleability", "Density", "Brittleness"], "answer": "Malleability"},
    {"q": "Which of these is NOT a property of metals?", "options": ["Low melting point", "High density", "Good conductor of heat"], "answer": "Low melting point"},
    {"q": "Which of these is a property of metals?", "options": ["Poor conductor of electricity", "High melting point", "Low density"], "answer": "High melting point"},

    # Physical Properties of Nonmetals
    {"q": "Which is a physical property of nonmetals?", "options": ["Shiny", "Dull", "Malleable"], "answer": "Dull"},
    {"q": "Which describes nonmetals?", "options": ["Good conductors", "Brittle", "High density"], "answer": "Brittle"},
    {"q": "Which is true of nonmetals?", "options": ["High melting point", "Poor conductor of electricity", "Luster"], "answer": "Poor conductor of electricity"},
    {"q": "Which is NOT a property of nonmetals?", "options": ["Low density", "Ductile", "Poor conductor of heat"], "answer": "Ductile"},
    {"q": "Which is a typical melting point behavior of nonmetals?", "options": ["High", "Low", "Variable"], "answer": "Low"},

    # Metalloids and Life Elements
    {"q": "Which group has properties between metals and nonmetals?", "options": ["Metalloids", "Halogens", "Alkali metals"], "answer": "Metalloids"},
    {"q": "Which element is commonly used in computer chips?", "options": ["Carbon", "Silicon", "Oxygen"], "answer": "Silicon"},
    {"q": "Which element makes life possible?", "options": ["Carbon", "Nitrogen", "Helium"], "answer": "Carbon"},
    {"q": "Which of these is NOT considered essential for life?", "options": ["Hydrogen", "Oxygen", "Neon"], "answer": "Neon"},
    {"q": "Which elements are important to life?", "options": ["Hydrogen, Nitrogen, Oxygen", "Helium, Argon, Krypton", "Sodium, Magnesium, Calcium"], "answer": "Hydrogen, Nitrogen, Oxygen"},
]

# -----------------------------
# QUIZ DISPLAY
# -----------------------------
user_answers = []
all_answered = True

# Load periodic table image once
st.image("Periodic_Table.png", width=600)

for i, q in enumerate(questions):
    st.markdown(f"<h2 style='font-size: 32px;'>Question {i+1}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 28px; font-weight: bold;'>{q['q']}</p>", unsafe_allow_html=True)

    options = [" "] + q["options"]
    choice = st.radio(
        "",
        options,
        index=0,
        key=f"q{i}",
        format_func=lambda x: f"   {x}" if x == " " else f"🔹 {x}"
    )

    user_answers.append(choice)
    if choice == " ":
        all_answered = False

    st.progress(int(((i + 1) / len(questions)) * 100))

# -----------------------------
# SUBMIT BUTTON
# -----------------------------
if st.button("Submit Quiz"):
    if not all_answered:
        st.error("Please answer all questions before submitting.")
    else:
        score = 0
        st.success("Quiz Submitted!")

        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size: 28px;'>Question {i+1}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 24px;'><b>Your answer:</b> {user_answers[i]}</p>", unsafe_allow_html=True)

            if user_answers[i] == q["answer"]:
                st.markdown("<span style='color:green; font-size:24px; font-weight:bold;'>Correct ✔</span>", unsafe_allow_html=True)
                score += 1
            else:
                st.markdown("<span style='color:red; font-size:24px; font-weight:bold;'>Incorrect ✘</span>", unsafe_allow_html=True)

            st.markdown(f"<p style='font-size: 22px;'><b>Correct answer:</b> {q['answer']}</p>", unsafe_allow_html=True)
            st.write("---")

        st.markdown(f"<h2 style='font-size: 32px;'>Final Score: {score} / {len(questions)}</h2>", unsafe_allow_html=True)

        if score == 25:
            st.success("🎉 Perfect score! You're a periodic table pro!")
        elif score >= 20:
            st.info("👏 Great job! You really understand the main group elements.")
        elif score >= 15:
            st.warning("👍 Good effort! Review the physical properties and group trends.")
        else:
            st.error("📘 Keep studying! Focus on group identification and element properties.")

        if st.button("Try Again"):
            st.session_state.clear()
            st.experimental_rerun()
