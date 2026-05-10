from src.hybrid_model import hybrid_analysis
from src.interpreter import interpret


def main():
    print("=== Cognitive Security Persuasion Analyzer ===")
    print()

    text = input("Enter a message to analyze: ")

    scores = hybrid_analysis(text)

    print("\nPersuasion Scores:")
    print("-------------------")

    for category, score in scores.items():
        print(f"{category}: {score}")

    print("\nInterpretation:")
    print("-------------------")

    insights = interpret(scores)

    for insight in insights:
        print(insight)


if __name__ == "__main__":
    main()
