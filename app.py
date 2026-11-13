from flask import Flask, render_template, request
from youtube_crawler import get_comments, save_comments
from analysis import load_comments, segment_text, create_wordcloud, get_top_words
from sentiment import analyze_sentiment, plot_sentiment
import matplotlib.pyplot as plt

app = Flask(__name__)


def generate_explanation(summary):
    if summary.get("Positive", 0) > summary.get("Negative", 0):
        return "Overall audience reaction is positive."
    elif summary.get("Positive", 0) < summary.get("Negative", 0):
        return "Overall audience reaction is negative."
    else:
        return "Audience reaction is mixed."


def create_comparison_chart(s1, s2):
    labels = ["Positive", "Neutral", "Negative"]

    song1 = [s1.get(k, 0) for k in labels]
    song2 = [s2.get(k, 0) for k in labels]

    x = range(len(labels))

    plt.figure()
    plt.bar(x, song1, width=0.4, label="Song 1")
    plt.bar([i + 0.4 for i in x], song2, width=0.4, label="Song 2")

    plt.xticks([i + 0.2 for i in x], labels)
    plt.legend()

    plt.title("Sentiment Comparison")
    plt.savefig("static/comparison.png")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        action = request.form["action"]

        if action == "single":
            url = request.form["song"]

            comments = get_comments(url)
            save_comments(comments)

            text = load_comments("data/comments.csv")
            segmented = segment_text(text)
            create_wordcloud(segmented)

            top_words = get_top_words(segmented)

            df, summary = analyze_sentiment()
            plot_sentiment(df)

            explanation = generate_explanation(summary)

            return render_template(
                "result.html",
                summary=summary,
                top_words=top_words,
                explanation=explanation
            )

        elif action == "compare":
            song1 = request.form["song1"]
            song2 = request.form["song2"]

            # Song 1
            comments1 = get_comments(song1)
            save_comments(comments1)
            df1, summary1 = analyze_sentiment()

            # Song 2
            comments2 = get_comments(song2)
            save_comments(comments2)
            df2, summary2 = analyze_sentiment()

            create_comparison_chart(summary1, summary2)

            return render_template(
                "compare.html",
                s1=summary1,
                s2=summary2
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)