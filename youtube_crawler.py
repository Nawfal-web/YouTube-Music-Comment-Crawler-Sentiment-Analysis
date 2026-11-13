from youtube_comment_downloader import YoutubeCommentDownloader
import csv
import os

def get_comments(video_url, max_comments=50):
    from youtube_comment_downloader import YoutubeCommentDownloader

    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(video_url)

    result = []
    for i, c in enumerate(comments):
        if i >= 100:
            break
        result.append(c["text"])

    return result


def save_comments(comments):
    os.makedirs("data", exist_ok=True)

    with open("data/comments.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Comment"])

        for c in comments:
            writer.writerow([c])

    print("Comments saved!")


if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    comments = get_comments(url)
    save_comments(comments)