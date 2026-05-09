import streamlit as st

def analyze(text):
    score = {
        "urgency": 0,
        "authority": 0,
        "emotion": 0,
        "trust": 0,
        "social": 0
    }

    t = text.lower()

    if "urgent" in t or "immediately" in t:
        score["urgency"] += 2

    if "official" in t or "bank" in t:
        score["authority"] += 2

    if "warning" in t or "fear" in t:
        score["emotion"] += 2

    if "trusted" in t:
        score["trust"] += 1

    if "everyone" in t or "others" in t:
        score["social"] += 2

    total = sum(score.values())

    return score, total


st.title("Adaptive AI Persuasion Explorer")

text = st.text_area("Enter message")

if st.button("Analyze"):
    score, total = analyze(text)

    st.write("### Breakdown")
    st.json(score)

    st.write("### Total Risk Score")
    st.metric("Risk", total)
