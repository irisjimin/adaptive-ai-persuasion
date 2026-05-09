import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Adaptive AI Persuasion Explorer",
    layout="centered"
)

# -----------------------------
# Semantic Embedding Model
# -----------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

prototypes = {
    "authority": "This is an official message from the government bank security team",
    "urgency": "Immediate action required or your account will be suspended",
    "emotion": "Your account is at risk and may be permanently lost",
    "social_pressure": "Most users have already verified their accounts",
    "trust_framing": "Please verify to ensure your safety and security"
}

prototype_embeddings = {
    k: model.encode(v)
    for k, v in prototypes.items()
}

# -----------------------------
# Rule-Based Analysis
# -----------------------------
def analyze_rule_based(text):
    text = text.lower()

    score = {
        "authority": 0,
        "urgency": 0,
        "emotion": 0,
        "social_pressure": 0,
        "trust_framing": 0
    }

    # Authority
    if any(w in text for w in [
        "bank", "official", "security",
        "government", "admin", "support team"
    ]):
        score["authority"] += 2

    # Urgency
    if any(w in text for w in [
        "urgent", "immediately", "now",
        "asap", "within 24 hours"
    ]):
        score["urgency"] += 2

    # Emotion / Fear
    if any(w in text for w in [
        "fear", "risk", "loss",
        "danger", "suspended",
        "problem", "permanent"
    ]):
        score["emotion"] += 2

    # Social Pressure
    if any(w in text for w in [
        "everyone", "others",
        "most users", "many users"
    ]):
        score["social_pressure"] += 2

    # Trust Framing
    if any(w in text for w in [
        "verify", "confirm",
        "secure", "protect",
        "safety"
    ]):
        score["trust_framing"] += 1

    # Clamp score (0–3)
    for k in score:
        score[k] = min(score[k], 3)

    return score

# -----------------------------
# Semantic Similarity Model
# -----------------------------
def semantic_score(text):
    emb = model.encode(text)

    semantic_scores = {}

    for k, proto_emb in prototype_embeddings.items():

        similarity = np.dot(emb, proto_emb) / (
            np.linalg.norm(emb) *
            np.linalg.norm(proto_emb)
        )

        semantic_scores[k] = round(float(similarity), 2)

    return semantic_scores

# -----------------------------
# Hybrid Fusion Model
# -----------------------------
def hybrid_analysis(text):

    rule_score = analyze_rule_based(text)
    semantic = semantic_score(text)

    hybrid = {}

    for k in rule_score:
        hybrid[k] = round(
            (rule_score[k] * 0.5) + (semantic[k] * 3),
            2
        )

    return hybrid

# -----------------------------
# Interpretation Layer
# -----------------------------
def interpret(scores):

    insights = []

    if scores["urgency"] >= 2:
        insights.append(
            "⚠️ High urgency framing detected → possible time-pressure manipulation"
        )

    if scores["authority"] >= 2:
        insights.append(
            "🏛 Authority framing detected → institutional legitimacy exploitation"
        )

    if scores["emotion"] >= 2:
        insights.append(
            "😨 Emotional pressure detected → fear/loss cognitive trigger"
        )

    if scores["social_pressure"] >= 2:
        insights.append(
            "👥 Social influence signal detected → conformity pressure"
        )

    if scores["trust_framing"] >= 1:
        insights.append(
            "🔐 Trust framing detected → legitimacy enhancement strategy"
        )

    if not insights:
        insights.append(
            "✅ No strong persuasion signals detected"
        )

    return insights

# -----------------------------
# Adversarial Dataset
# -----------------------------
adversarial_samples = [
    "URGENT: Your bank account will be suspended immediately",
    "You must verify now or lose access forever",
    "Most users already confirmed their identity",
    "Official security alert from government system",
    "Failure to comply will result in permanent restriction"
]

# -----------------------------
# UI
# -----------------------------
st.title("🧠 Adaptive AI Persuasion Explorer")

st.write(
    """
Explainable cognitive analysis of persuasive communication
using a hybrid rule-based + semantic embedding framework.
"""
)

st.markdown("---")

text = st.text_area(
    "Enter a message for persuasion analysis"
)

# -----------------------------
# Main Analysis
# -----------------------------
if st.button("Analyze Message"):

    scores = hybrid_analysis(text)

    st.subheader("📊 Persuasion Signal Scores")

    for k, v in scores.items():
        st.write(f"**{k}**: {v}")

    # -------------------------
    # Visualization
    # -------------------------
    st.subheader("📈 Visualization")

    df = pd.DataFrame({
        "Feature": list(scores.keys()),
        "Score": list(scores.values())
    })

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Feature", sort=None),
        y="Score",
        color="Feature"
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )

    # -------------------------
    # Interpretation Layer
    # -------------------------
    st.subheader("🧠 Interpretation Layer")

    insights = interpret(scores)

    for insight in insights:
        st.write(insight)

# -----------------------------
# Adversarial Evaluation
# -----------------------------
st.markdown("---")

st.subheader("🧪 Adversarial Prompt Evaluation")

if st.button("Run Adversarial Dataset"):

    for i, sample in enumerate(adversarial_samples):

        st.markdown(f"### Sample {i+1}")

        st.write(sample)

        sample_score = hybrid_analysis(sample)

        st.json(sample_score)
