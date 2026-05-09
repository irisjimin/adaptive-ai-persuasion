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

    if any(w in text for w in ["urgent", "immediately", "now", "asap"]):
        score["urgency"] += 2

    if any(w in text for w in ["bank", "official", "security", "government"]):
        score["authority"] += 2

    if any(w in text for w in ["fear", "risk", "loss", "danger", "suspended"]):
        score["emotion"] += 2

    if any(w in text for w in ["everyone", "others", "most users"]):
        score["social_pressure"] += 2

    if any(w in text for w in ["verify", "confirm", "secure", "protect"]):
        score["trust_framing"] += 1

    for k in score:
        score[k] = min(score[k], 3)

    return score


# -----------------------------
# 2. Interpretation Layer (CHI 핵심 추가)
# -----------------------------
def interpret(score):
    insights = []

    if score["urgency"] >= 2:
        insights.append("⚠️ High urgency detected → time-pressure manipulation likely")

    if score["authority"] >= 2:
        insights.append("🏛 Authority framing detected → institutional trust exploitation")

    if score["emotion"] >= 2:
        insights.append("😨 Emotional fear framing → cognitive bias activation")

    if score["social_pressure"] >= 2:
        insights.append("👥 Social proof pressure → conformity bias trigger")

    if score["trust_framing"] >= 1:
        insights.append("🔐 Trust framing → legitimacy enhancement strategy")

    if not insights:
        insights.append("✅ No strong persuasion patterns detected")

    return insights


# -----------------------------
# 3. UI
# -----------------------------
st.title("🧠 Adaptive AI Persuasion Explorer")
st.write("Explainable cognitive analysis of persuasive communication (rule-based model)")

text = st.text_area("Enter message")

if st.button("Analyze"):
    result = analyze(text)

    st.subheader("📊 Persuasion Signals")

    for k, v in result.items():
        st.write(f"**{k}**: {v}")

    st.subheader("🧠 Interpretation Layer")

    for line in interpret(result):
        st.write(line)
