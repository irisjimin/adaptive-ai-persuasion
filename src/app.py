import streamlit as st
import pandas as pd
import altair as alt

from hybrid_model import hybrid_analysis
from interpreter import interpret


st.set_page_config(
    page_title="Adaptive AI Persuasion Explorer",
    layout="centered"
)

st.title("🧠 Cognitive Security Persuasion Explorer")

st.write(
    """
Analyze persuasive language patterns in potentially manipulative messages
using a hybrid explainable AI framework.
"""
)

st.markdown("---")

text = st.text_area(
    "Enter a message for analysis"
)

if st.button("Analyze Message"):

    if not text.strip():
        st.warning("Please enter a message.")
    else:
        scores = hybrid_analysis(text)

        st.subheader("📊 Persuasion Signal Scores")

        for category, score in scores.items():
            st.write(f"**{category}**: {score}")

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

        st.subheader("🧠 Interpretation Layer")

        insights = interpret(scores)

        for insight in insights:
            st.write(insight)
