# Cognitive Security for AI-Generated Persuasion
### Explainable Detection of Psychological Manipulation in LLM-Generated Text

## Overview

Large Language Models are increasingly capable of generating persuasive content that can influence human cognition, trust, and decision-making.

This creates emerging risks in:

- AI-generated phishing
- social engineering attacks
- manipulative chatbot interactions
- deceptive automated messaging

Most existing safety systems focus on binary harmful/not harmful classification, which often fails to explain *how* persuasion operates.

This project introduces an interpretable cognitive security framework that decomposes persuasive language into structured psychological influence signals.

The system identifies:

- Authority framing
- Urgency pressure
- Emotional manipulation
- Social pressure
- Trust framing

and provides human-readable explanations for why a message may be psychologically manipulative.

---

## Research Motivation

As generative AI systems become more accessible, malicious actors may increasingly use LLMs to create scalable phishing campaigns, fraud messages, and social engineering attacks.

Traditional content moderation systems often detect whether content is harmful, but they rarely explain the underlying persuasion mechanisms used to manipulate users.

This project explores a different question:

**Can AI systems help explain cognitive manipulation strategies embedded in persuasive language?**

---

## Research Question

How can we build interpretable systems that detect and explain persuasion strategies used in AI-generated manipulative communication?

---

## Methodology

This project uses a hybrid architecture that combines symbolic reasoning with semantic modeling.

### 1. Rule-Based Persuasion Detection

Keyword-level heuristics identify explicit persuasion indicators such as:

- urgency terms
- authority claims
- fear triggers
- trust language
- conformity pressure

---

### 2. Semantic Similarity Layer

To reduce limitations of pure keyword detection, the system uses:

`sentence-transformers/all-MiniLM-L6-v2`

to compare input messages against persuasion prototypes using embedding similarity.

This enables detection of semantically similar manipulative language patterns.

---

### 3. Hybrid Scoring Model

Final persuasion scores combine:

- rule-based signals
- semantic similarity scores

to improve interpretability while maintaining flexibility.

---

### 4. Interpretation Layer

The system converts numerical scores into human-readable explanations such as:

- "High urgency framing detected"
- "Authority exploitation detected"
- "Emotional pressure identified"

---

## System Architecture

```bash
Input Message
    ↓
Rule-Based Detection
    ↓
Semantic Embedding Analysis
    ↓
Hybrid Score Fusion
    ↓
Interpretation Layer
    ↓
Visualization Dashboard


## Installation

Clone the repository:

```bash
git clone https://github.com/irisjimin/adaptive-ai-persuasion.git
cd adaptive-ai-persuasion
