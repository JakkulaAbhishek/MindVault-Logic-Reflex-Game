import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MindVault Game",
    page_icon="🧠",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    font-family: 'Segoe UI', sans-serif;
}
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.big {
    font-size: 32px;
    font-weight: 700;
}
.score {
    font-size: 22px;
    color: #0f5132;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='big'>🧠 MindVault – Brain & Reflex Game</div>", unsafe_allow_html=True)
st.write("Train your **logic, memory & reaction speed** 🚀")

st.markdown(f"<div class='score'>🎯 Score: {st.session_state.score}</div>", unsafe_allow_html=True)
st.divider()

# ---------------- GAME MODE SELECT ----------------
mode = st.selectbox(
    "🎮 Select Game Mode",
    ["Quick Math", "Memory Pattern", "Reaction Speed"]
)

# ---------------- QUICK MATH ----------------
if mode == "Quick Math":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    operator = random.choice(["+", "-", "*"])

    question = f"{a} {operator} {b}"
    correct = eval(question)

    st.subheader("🧮 Solve Quickly!")
    answer = st.number_input(f"{question} = ?", step=1)

    if st.button("Submit Answer"):
        if answer == correct:
            st.success("✅ Correct!")
            st.session_state.score += 10
        else:
            st.error(f"❌ Wrong! Correct Answer: {correct}")
            st.session_state.score -= 5
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MEMORY GAME ----------------
elif mode == "Memory Pattern":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧩 Memory Challenge")

    pattern = [random.randint(1, 9) for _ in range(5)]
    st.write("Memorize this pattern 👀")
    st.code("  ".join(map(str, pattern)))

    time.sleep(3)
    st.write("Now enter the pattern 👇")

    user_input = st.text_input("Enter numbers separated by space")

    if st.button("Check Memory"):
        try:
            user_pattern = list(map(int, user_input.split()))
            if user_pattern == pattern:
                st.success("🧠 Perfect Memory!")
                st.session_state.score += 15
            else:
                st.error(f"❌ Wrong! Pattern was {pattern}")
                st.session_state.score -= 5
        except:
            st.warning("⚠️ Invalid input")
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- REACTION SPEED ----------------
elif mode == "Reaction Speed":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("⚡ Reaction Speed Test")

    if st.button("Start Test"):
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)
        st.session_state.start_time = time.time()
        st.warning("CLICK NOW!")

    if st.session_state.start_time:
        if st.button("CLICK!"):
            reaction = time.time() - st.session_state.start_time
            st.session_state.start_time = None

            st.info(f"⏱ Reaction Time: {reaction:.3f} seconds")

            if reaction < 0.4:
                st.success("🔥 Lightning Fast!")
                st.session_state.score += 20
            elif reaction < 0.8:
                st.success("👍 Good Reflex!")
                st.session_state.score += 10
            else:
                st.warning("🐢 Too Slow!")
                st.session_state.score += 2

            st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
st.markdown("🚀 **Tip:** Faster + Accurate = Higher Score")
st.caption("Built with ❤️ using Streamlit")
