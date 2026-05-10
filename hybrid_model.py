from rules import analyze_rule_based
from semantic_model import semantic_score

def hybrid_analysis(text):
    rule = analyze_rule_based(text)
    semantic = semantic_score(text)

    return {**rule, **semantic}