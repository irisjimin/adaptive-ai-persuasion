# Cognitive Security for AI-Generated Persuasion
### Explainable Detection of Psychological Manipulation in LLM-Generated Text

## Overview

Large Language Models can generate highly persuasive content capable of influencing human trust, decision-making, and behavior.

This creates emerging risks in:

- AI-generated phishing attacks
- social engineering campaigns
- manipulative chatbot interactions
- deceptive automated messaging

Most existing safety systems focus on binary harmful/not harmful classification, but fail to explain **how persuasion works**.

This project introduces an interpretable cognitive security framework that decomposes persuasive language into structured psychological influence signals.

The system identifies:

- Authority framing
- Urgency pressure
- Emotional manipulation
- Social pressure
- Trust framing

and generates human-readable explanations for why a message may be psychologically manipulative.

---

# Demo Preview

![Demo](assets/demo.gif)

---

# Research Motivation

As generative AI systems become more accessible, malicious actors may increasingly use LLMs to scale phishing campaigns, fraud attempts, and social engineering attacks.

Traditional moderation systems often detect whether content is harmful, but rarely explain the underlying persuasion mechanisms used to manipulate users.

This project explores a different question:

**Can AI systems help explain cognitive manipulation strategies embedded in persuasive language?**

---

# Research Question

How can we build interpretable systems that detect and explain persuasion strategies used in AI-generated manipulative communication?

---

# Methodology

This project uses a hybrid architecture combining symbolic reasoning and semantic modeling.

---

## 1. Rule-Based Detection

Keyword heuristics identify explicit persuasion indicators such as:

- urgency terms
- authority claims
- fear triggers
- trust language
- conformity pressure

Implemented in:

```bash
src/rules.py
