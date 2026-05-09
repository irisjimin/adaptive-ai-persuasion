import streamlit as st
import re

st.set_page_config(page_title="AI Persuasion Lab", layout="centered")

# -----------------------------
# 1. Cognitive feature extractor
# -----------------------------
def analyze(text):
    text_lower = text.lower()

    score = {
        "authority": 0,
        "urgency": 0,
        "emotion": 0,
        "social_pressure": 0,
        "trust_framing": 0,
    }

    # -----------------------------
    # 2. Rule-based heuristics
    # -----------------------------

    # urgency signals
    if any(word in text_lower for word in ["urgent", "immediately", "now", "asap", "right away"]):
        score["urgency"] += 2

    if re.search(r"24 hours|today only|limited time", text_lower):
        score["urgency"] += 1

    # authority signals
    if any(word in text_lower for word in ["bank", "official", "security team", "government"]):
        score["authority"] += 2

    # emotion signals
    if any(word in text_lower for word in ["worried", "afraid", "risk", "loss", "problem"]):
        score["emotion"] += 2

    # social pressure
    if any(word in text_lower for word in ["everyone", "most users", "people are", "others have"]):
        score["social_pressure"] += 2

    # trust framing
    if any(word in text_lower for word in ["verify", "confirm", "secure", "protect", "help us"]):
        score["trust_framing"] += 1

    # clamp values (0–3)
    for k in score:
        score[k] = min(score[k], 3)

    return score


# -----------------------------
# UI
# -----------------------------
st.title("🧠 Adaptive AI Persuasion Explorer")
st.write("Rule-based cognitive analysis of persuasive communication")

text = st.text_area("Enter message")

if st.button("Analyze"):
    score = analyze(text)

    st.subheader("Psychological Influence Breakdown")

    for k, v in score.items():
        st.write(f"**{k}**: {v}")

    st.subheader("Interpretation")

    if score["urgency"] >= 2:
        st.write("High urgency detected: time pressure is used to influence decision-making.")

    if score["authority"] >= 2:
        st.write("Authority framing detected: message simulates institutional legitimacy.")

    if score["emotion"] >= 2:
        st.write("Emotional manipulation detected: negative affect is leveraged.")

    if sum(score.values()) == 0:
        st.write("No strong persuasion signals detected.")
