import streamlit as st

st.set_page_config(page_title="Adaptive AI Persuasion Explorer", layout="centered")


# -----------------------------
# 1. Feature Extraction Model
# -----------------------------
def analyze(text):
    text = text.lower()

    score = {
        "authority": 0,
        "urgency": 0,
        "emotion": 0,
        "social_pressure": 0,
        "trust_framing": 0
    }

    # Urgency signals
    if any(w in text for w in ["urgent", "immediately", "now", "asap"]):
        score["urgency"] += 2

    # Authority signals
    if any(w in text for w in ["bank", "official", "security", "government"]):
        score["authority"] += 2

    # Emotion / fear signals
    if any(w in text for w in ["fear", "risk", "loss", "danger", "suspended"]):
        score["emotion"] += 2

    # Social pressure
    if any(w in text for w in ["everyone", "others", "most users"]):
        score["social_pressure"] += 2

    # Trust framing
    if any(w in text for w in ["verify", "confirm", "secure", "protect"]):
        score["trust_framing"] += 1

    # Clamp (0–3)
    for k in score:
        score[k] = min(score[k], 3)

    return score


# -----------------------------
# 2. UI
# -----------------------------
st.title("🧠 Adaptive AI Persuasion Explorer")
st.write("Explainable cognitive analysis of persuasive communication (rule-based model)")

text = st.text_area("Enter message")

if st.button("Analyze"):
    result = analyze(text)

    st.subheader("Results")

    for k, v in result.items():
        st.write(f"**{k}**: {v}")