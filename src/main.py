# Adaptive AI Persuasion Explorer (prototype)

def analyze_persuasion(text):
    score = {
        "urgency": 0,
        "authority": 0,
        "emotion": 0,
        "trust": 0
    }

    text_lower = text.lower()

    # simple heuristic model (research prototype stage)
    if "urgent" in text_lower or "immediately" in text_lower:
        score["urgency"] += 2

    if "bank" in text_lower or "official" in text_lower:
        score["authority"] += 2

    if "angry" in text_lower or "warning" in text_lower:
        score["emotion"] += 2

    if "trusted" in text_lower or "secure" in text_lower:
        score["trust"] += 1

    total = sum(score.values())

    return {
        "scores": score,
        "total_manipulation_risk": total
    }


# demo run
if __name__ == "__main__":
    sample = "Urgent: Your bank account will be suspended immediately"
    result = analyze_persuasion(sample)

    print("INPUT:", sample)
    print("ANALYSIS:", result)
