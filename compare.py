from youtube_crawler import get_comments, save_comments
from sentiment import analyze_sentiment


def analyze_song(song_url):
    print(f"\nAnalyzing: {song_url}")

    comments = get_comments(song_url)

    if not comments:
        print(" Failed to fetch comments")
        return None

    print(f" Got {len(comments)} comments")

    # Save to file
    save_comments(comments)

    # Analyze
    df, summary = analyze_sentiment()

    print(f"✅ Summary: {summary}")

    return summary


def compare_songs(song1, song2):
    result1 = analyze_song(song1)
    result2 = analyze_song(song2)

    if result1 is None or result2 is None:
        print(" Error in analysis")
        return

    print("\n=== COMPARISON ===")

    print("\nSong 1:")
    for k, v in result1.items():
        print(f"{k}: {v}%")

    print("\nSong 2:")
    for k, v in result2.items():
        print(f"{k}: {v}%")

    print("\n=== INSIGHT ===")

    if result1.get("Positive", 0) > result2.get("Positive", 0):
        print(" Song 1 is more positively received")
    elif result1.get("Positive", 0) < result2.get("Positive", 0):
        print(" Song 2 is more positively received")
    else:
        print(" Both songs have similar positive reception")


if __name__ == "__main__":
    song1 = input("Enter first song URL: ")
    song2 = input("Enter second song URL: ")

    compare_songs(song1, song2)