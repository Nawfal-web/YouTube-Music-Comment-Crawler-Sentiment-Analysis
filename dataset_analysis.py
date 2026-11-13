from analysis import load_comments, segment_text, create_wordcloud, get_top_words
from sentiment import analyze_sentiment, plot_sentiment


def analyze_dataset(filepath):

    print(f"\nAnalyzing dataset: {filepath}")

    text = load_comments(filepath)

    segmented = segment_text(text)

    create_wordcloud(segmented)

    top_words = get_top_words(segmented)

    topics = detect_topics(segmented)

    print("\nTopic Analysis:")
    print(topics)

    df, summary = analyze_sentiment()

    print("\nSummary:")
    print(summary)

    print("\nTop Words:")
    for word, count in top_words:
        print(word, count)

    plot_sentiment(df)

    return summary

def detect_topics(text):

    categories = {
        "Emotion": ["love", "sad", "happy", "cry", "feel"],
        "Music": ["song", "music", "beat", "sound"],
        "Performance": ["dance", "voice", "performance"],
        "Gaming": ["fifa", "mobile", "game"]
    }

    results = {}

    words = text.split()

    for category, keywords in categories.items():

        count = 0

        for word in words:
            if word in keywords:
                count += 1

        results[category] = count

    return results

if __name__ == "__main__":
    analyze_dataset("dataset/billie_jean.csv")