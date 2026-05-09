import streamlit as st

st.set_page_config(page_title="AI Persuasion Lab", layout="centered")

def analyze(text):
    score = {
        "Authority": 0,
        "Emotion": 0,
        "Urgency": 0,
        "Social Pressure": 0,
        "Trust Framing": 0
    }

    t = text.lower()

    if "urgent" in t:
        score["Urgency"] += 2
    if "official" in t or "bank" in t:
        score["Authority"] += 2
    if "warning" in t or "fear" in t:
        score["Emotion"] += 2
    if "everyone" in t or "others" in t:
        score["Social Pressure"] += 2
    if "trusted" in t:
        score["Trust Framing"] += 1

    return score


st.title("🧠 Adaptive AI Persuasion Explorer")
st.write("Analyzing how AI-driven messages manipulate human decision-making")

text = st.text_area("Enter message")

if st.button("Analyze"):
    score = analyze(text)

    st.subheader("Psychological Influence Breakdown")

    for k, v in score.items():
        st.write(f"**{k}**: {v}")

    st.subheader("Interpretation")
    st.write("This message contains layered persuasion signals affecting human cognitive bias.")
