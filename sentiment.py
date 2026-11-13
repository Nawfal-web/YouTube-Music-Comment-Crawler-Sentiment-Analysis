print("THIS IS THE NEW FILE")

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


def analyze_sentiment():

    df = pd.read_csv("data/comments.csv")

    sentiments = []

    analyzer = SentimentIntensityAnalyzer()

    for comment in df["Comment"].astype(str):

        score = analyzer.polarity_scores(comment)["compound"]

        if score >= 0.05:
            sentiments.append("Positive")

        elif score <= -0.05:
            sentiments.append("Negative")

        else:
            sentiments.append("Neutral")

    df["Sentiment"] = sentiments

    counts = df["Sentiment"].value_counts()
    total = len(df)

    summary = {}

    for sentiment, count in counts.items():
        summary[sentiment] = round((count / total) * 100, 1)

    return df, summary


def plot_sentiment(df):

    counts = df["Sentiment"].value_counts()

    total = len(df)

    print("\n--- Sentiment Summary ---")
    for sentiment, count in counts.items():
        percentage = (count / total) * 100
        print(f"{sentiment}: {count} ({percentage:.1f}%)")

    plt.figure(figsize=(6,4))

    counts.plot(kind="bar")

    plt.title("Sentiment Analysis of Comments")
    plt.xlabel("Sentiment Type")
    plt.ylabel("Number of Comments")

    plt.tight_layout()

    plt.savefig("static/sentiment.png")

    plt.close()

    print("\nChart saved to static/sentiment.png")


def sentiment_trend(df):

    scores = df["Sentiment"].map({
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1
    })

    plt.figure(figsize=(8,4))

    plt.plot(scores.values)

    plt.title("Sentiment Trend Over Comments")
    plt.xlabel("Comment Index")
    plt.ylabel("Sentiment Score")

    plt.tight_layout()

    plt.savefig("static/sentiment_trend.png")

    plt.close()

    print("Sentiment trend saved!")


if __name__ == "__main__":

    df, summary = analyze_sentiment()

    print("\n--- Summary ---")
    print(summary)

    plot_sentiment(df)

    sentiment_trend(df)