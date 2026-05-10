# Cognitive Security for AI-Generated Persuasion
### Explainable Detection of Psychological Manipulation in LLM-Generated Text

## Overview

Large Language Models can generate highly persuasive content capable of influencing human trust, decision-making, and behavior.

This creates emerging risks in:

- AI-generated phishing attacks
- social engineering campaigns
- manipulative chatbot interactions
- deceptive automated messaging

Most existing safety systems focus on binary harmful/not harmful classification but fail to explain how persuasion works.

This project introduces an interpretable cognitive security framework that decomposes persuasive language into structured psychological influence signals.

## Demo Preview
![Demo](assets/demo.gif)

## Research Motivation

As generative AI systems become more accessible, malicious actors may increasingly use LLMs to scale phishing campaigns, fraud attempts, and social engineering attacks.

Traditional moderation systems often detect harmful outputs but rarely explain the underlying persuasion mechanisms used to manipulate users.

## Research Question

How can we build interpretable systems that detect and explain persuasion strategies used in AI-generated manipulative communication?

## Methodology
This project uses a hybrid architecture combining symbolic reasoning and semantic modeling.

### Rule-Based Detection

Keyword heuristics identify explicit persuasion indicators such as:

- authority claims
- urgency language
- emotional pressure
- social conformity
- trust framing

Implemented in:

src/rules.py

### Semantic Similarity Layer

The system uses:

sentence-transformers/all-MiniLM-L6-v2

to compare input messages against persuasion prototypes using embedding similarity.

Implemented in:

src/semantic_model.py

### Hybrid Score Fusion

Final persuasion scores combine:

- rule-based signals
- semantic similarity signals

Implemented in:

src/hybrid_model.py

### Interpretation Layer

The system converts numerical outputs into human-readable explanations such as:

- High urgency manipulation detected
- Authority exploitation detected
- Emotional manipulation identified

Implemented in:

src/interpreter.py

## System Architecture
![Architecture](assets/architecture.png)

## Interactive Dashboard

Built with:

- Streamlit
- Altair
- Python
- Sentence Transformers

Implemented in:

src/app.py

## CLI Analysis

A lightweight command-line version is included for quick experimentation.

Implemented in:

src/main.py

## Evaluation

This repository includes synthetic adversarial persuasion testing.

Dataset:

data/synthetic_prompts.csv

Evaluation pipeline:

src/evaluator.py

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

## Current Limitations

This project is an early-stage research prototype.

Current limitations include:

- small evaluation dataset
- synthetic prompts
- limited benchmark testing
- English-only evaluation
- handcrafted persuasion taxonomy

## Future Work

Future improvements include:

- real phishing dataset evaluation
- multilingual persuasion detection
- LLM-generated scam detection
- benchmark comparison with larger safety models

## Repository Structure

adaptive-ai-persuasion/
│
├── assets/
├── data/
├── src/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

## Installation

git clone https://github.com/irisjimin/adaptive-ai-persuasion.git
cd adaptive-ai-persuasion

pip install -r requirements.txt

## Run Interactive Demo

streamlit run src/app.py

## Run CLI Analysis

python src/main.py

## Run Evaluation Benchmark

python src/evaluator.py

## Ethical Notice
This repository is intended for defensive AI safety and cybersecurity research only.

It is designed to improve interpretability of manipulative language detection and is not intended to generate harmful persuasive content.

## Run Evaluation Benchmark

## Ethical Notice
