from crawler import search_song, get_comments, save_comments
from analysis import load_comments, segment_text, create_wordcloud
from sentiment import analyze_sentiment, plot_sentiment

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    
    print("Fetching comments...")   
    
    comments = get_comments(url)
    
    print(f"Got {len(comments)} comments")  
    
    save_comments(comments)

    # Step 1: Crawl
    song_id = search_song(song_name)
    print("Song ID:", song_id)

    if song_id:
        comments = get_comments(song_id)
        save_comments(comments)

        # Step 2: Word cloud
        text = load_comments()
        segmented = segment_text(text)
        create_wordcloud(segmented)

        # Step 3: Sentiment
        df = analyze_sentiment()
        plot_sentiment(df)

        print("\n Project completed!")
        print("Check output folder for results.")