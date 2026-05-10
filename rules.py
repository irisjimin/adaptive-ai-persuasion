def analyze_rule_based(text):
    text = text.lower()

    return {
        "authority": int("bank" in text),
        "urgency": int("urgent" in text),
        "emotion": int("risk" in text),
        "social_pressure": int("everyone" in text),
        "trust": int("verify" in text),
    }