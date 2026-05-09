# Adaptive AI Persuasion Explorer

## Abstract
## CCS Concepts (optional but strong)
## 1. Introduction
## 2. Problem Statement
## 3. System Design
## 4. Methodology
## 5. Implementation
## 6. Results (Demo)
## 7. Discussion
## 8. Limitations
## 9. Conclusion

## Abstract 
Large Language Models are increasingly capable of generating persuasive and adaptive communication that can influence human cognitive and behavioral responses. However, existing detection systems primarily focus on binary classification of malicious content, failing to model the underlying mechanisms of persuasion. This project introduces a human-centered security framework that decomposes AI-generated messages into interpretable cognitive influence signals, including authority, urgency, emotional pressure, social proof, and trust framing. By leveraging LLM-based reasoning, the system provides structured explanations of how persuasion is constructed rather than merely classifying messages as safe or unsafe. We present an interactive prototype built with Streamlit that visualizes these persuasion components in real time, enabling exploratory analysis of AI-mediated manipulation strategies in digital communication.

## CCS Concepts

- Security and privacy → Social engineering attacks
- Human-centered computing → HCI design and evaluation methods
- Computing methodologies → Natural language processing
- Information systems → Data mining for user behavior analysis


## 1. Introduction

Large Language Models increasingly generate persuasive content that can influence human decision-making. However, most existing systems treat such content as a binary classification problem (e.g., scam vs. safe), which fails to capture the underlying cognitive mechanisms of persuasion.

## 2. Problem Statement

Current AI safety and security tools focus on detection rather than explanation. As a result, users and researchers lack visibility into how persuasion is constructed within AI-generated communication.
This work investigates AI-mediated persuasion as a structured cognitive process and proposes a system that decomposes persuasive messages into interpretable psychological influence signals.

## 3. System Design

We model persuasion as a set of cognitive influence dimensions:

- Authority
- Urgency
- Emotion
- Social Pressure
- Trust Framing

The system decomposes input text into these signals using LLM-based reasoning and provides structured interpretability outputs.

## 4. Methodology

Instead of rule-based detection, we leverage large language models to infer latent persuasion structures. Each input message is analyzed through a reasoning prompt that extracts cognitive influence scores and explanatory interpretations.

## Key Contributions

- A shift from binary classification to structural persuasion modeling
- LLM-based interpretability of cognitive manipulation signals
- A human-centered security interface for analyzing AI-generated persuasion
