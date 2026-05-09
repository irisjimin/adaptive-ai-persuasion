import streamlit as st
import re

st.set_page_config(page_title="Adaptive AI Persuasion Explorer", layout="centered")

# -----------------------------
# 1. Feature Extraction Model
# -----------------------------
def extract_features(text):
    text = text.lower()

    features = {
        "authority": 0,
        "urgency": 0,
        "emotion": 0,
        "social_pressure": 0,
        "trust_framing": 0
    }

    # -------------------------
    # Authority signals
    # -------------------------
    authority_keywords = ["bank", "official", "security", "government", "admin", "support team"]
    if any(w in text for w in authority_keywords):
        features["authority"] += 2

    # -------------------------
    # Urgency signals
    # -------------------------
    urgency_keywords = ["urgent", "immediately", "now", "asap", "within 24 hours", "limited time"]
    if any(w in text for w in urgency_keywords):
        features["urgency"] += 2

    # -------------------------
    # Emotion / fear signals
    # -------------------------
    emotion_keywords = ["fear", "risk", "loss", "afraid", "danger", "suspended", "problem"]
    if any(w in text for w in emotion_keywords):
        features["emotion"] += 2

    # -------------------------
    # Social pressure
    # -------------------------
    social_keywords = ["everyone", "others", "most users", "people are", "many users"]
    if any(w in text for w in social_keywords):
        features["social_pressure"] += 2

    # -------------------------
    # Trust framing
    # -------------------------
    trust_keywords = ["verify", "confirm", "secure", "protect", "safety", "help us"]
    if any(w in text for w in trust_keywords):
        features["trust_framing"] += 1

    # Clamp (0–3)
    for k in features:
        features[k] = min(features[k], 3)

    return features


# -----------------------------
# 2. Interpretation Engine
# -----------------------------
def interpret(features):
    explanations = []

    if features["urgency"] >= 2:
        explanations.append("High urgency framing detected → time pressure manipulation likely.")

    if features["authority"] >= 2:
        explanations.append("Authority signal detected → institutional legitimacy imitation.")

    if features["emotion"] >= 2:
        explanations.append("Emotional manipulation detected → fear or loss framing present.")

    if features["social_pressure"] >= 2:
        explanations.append("Social influence detected → normative pressure applied.")

    if features["trust_framing"] >= 1:
        explanations.append("Trust framing present → attempts to increase perceived legitimacy.")

    if not explanations:
        explanations.append("No strong persuasion signals detected.")

    return explanations


# -----------------------------
# 3. UI
# -----------------------------
st.title("🧠 Adaptive AI Persuasion Explorer")
st.write("Explainable cognitive analysis of persuasive communication (rule-based model)")

text = st.text_area("Enter message")

if st.button("Analyze"):
    features = extract_features(text)
    interpretation = interpret(features)

    st.subheader("Psychological Influence Breakdown")

    for k, v in features.items():
        st.write(f"**{k}**: {v}")

    st.subheader("Interpretation")

    for line in interpretation:
        st.write("• " + line)
