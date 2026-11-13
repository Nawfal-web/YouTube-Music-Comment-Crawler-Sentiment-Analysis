import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import re


def load_comments(filepath):
    df = pd.read_csv(filepath)
    text = " ".join(df["Comment"].astype(str))
    return text

def segment_text(text):
    # extract English words only
    words = re.findall(r"[a-zA-Z]+", text.lower())

    # better stopwords list
    stopwords = [
    "the","and","is","to","of","in","it","this","that","i","you",
    "for","on","with","was","are","but","not","they","have","has",
    "had","just","like","get","got","one","all","can","will",
    "now","about","after","from","your","their"
]
    words = [w for w in words if w not in stopwords and len(w) > 2]

    return " ".join(words)

def create_wordcloud(text):
    from wordcloud import WordCloud

    wc = WordCloud(
    width=900,
    height=500,
    background_color="white",
    max_words=100,
    colormap="viridis"
    ).generate(text)

    wc.to_file("static/wordcloud.png")
    print("Word cloud saved!")

def top_words(text, n=10):
    words = text.split()
    counts = Counter(words)

    print("\nTop words:")
    for word, count in counts.most_common(n):
        print(f"{word}: {count}")    

def get_top_words(text, n=10):
    from collections import Counter
    words = text.split()
    counts = Counter(words)
    return counts.most_common(n)

if __name__ == "__main__":
    text = load_comments()
    segmented = segment_text(text)

    top_words(segmented) 

    create_wordcloud(segmented)


