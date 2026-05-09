# Adaptive AI Persuasion Explorer

## Research Problem
Modern AI systems are increasingly capable of generating highly persuasive messages that exploit human cognitive and emotional vulnerabilities. Existing security approaches primarily focus on binary classification (e.g., scam vs. safe), but fail to explain the underlying mechanisms of persuasion.

This project investigates how AI-mediated communication constructs adaptive persuasion strategies and how these strategies influence human security-related decision-making.

## Research Objective
The goal of this project is to model persuasion not as a classification problem, but as a structured cognitive process that evolves through multiple psychological influence signals.

We aim to understand how different combinations of persuasion cues affect perceived trust and decision behavior.

## Core Research Idea
Instead of detecting whether a message is “safe” or “unsafe”, we decompose persuasion into interpretable influence dimensions:

- authority signaling
- emotional pressure
- urgency framing
- social proof dynamics
- trust construction

We further explore how combinations of these signals produce layered manipulation effects.

## System Overview
The system takes digital messages as input and decomposes them into structured persuasion components.

It models:
- individual influence signals
- interaction effects between signals
- overall manipulation intensity

The output is an interpretable representation of how persuasion is constructed within the message.

## Dataset Design
The dataset is structured to isolate and combine psychological persuasion vectors (authority, emotion, social pressure) in order to analyze both single-factor and multi-factor manipulation patterns.

## Current Status
This is an early-stage research prototype focused on conceptual modeling, dataset design, and system-level interpretation of AI-driven persuasion.

## How to Run

To run the interactive demo locally:

```bash
pip install streamlit
streamlit run src/app.py
