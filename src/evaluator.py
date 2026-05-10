import os
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from hybrid_model import hybrid_analysis


def predict_label(text):
    scores = hybrid_analysis(text)

    if max(scores.values()) >= 2:
        return 1
    return 0


def evaluate():
    # robust path handling
    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATA_PATH = os.path.join(
        BASE_DIR,
        "data",
        "synthetic_prompts.csv"
    )

    df = pd.read_csv(DATA_PATH)

    predictions = []

    for text in df["text"]:
        pred = predict_label(text)
        predictions.append(pred)

    y_true = df["label"]

    print("Accuracy:", accuracy_score(y_true, predictions))
    print("Precision:", precision_score(y_true, predictions))
    print("Recall:", recall_score(y_true, predictions))
    print("F1 Score:", f1_score(y_true, predictions))


if __name__ == "__main__":
    evaluate()
