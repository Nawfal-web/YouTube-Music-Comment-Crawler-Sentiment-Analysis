print("RUNNING NOW")

import requests

def search_song(song_name):
    url = "https://music.163.com/api/search/get"
    
    data = {
        "s": song_name,
        "type": 1
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        print("Status:", response.status_code)

        result = response.json()
        print("Got response")

        songs = result.get("result", {}).get("songs", [])
        
        if not songs:
            print("No song found.")
            return None
        
        return songs[0]["id"]

    except Exception as e:
        print("Error:", e)
        return None

def get_comments(song_id, limit=20):
        url = f"https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}?limit={limit}"
    
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
    
        response = requests.get(url, headers=headers)
        data = response.json()
    
        comments = data.get("comments", [])
    
        return comments

def save_comments(comments):
    import os
    import csv

    os.makedirs("data", exist_ok=True)

    with open("data/comments.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["User", "Comment", "Likes"])

        for c in comments:
            user = c["user"]["nickname"]
            content = c["content"]
            likes = c["likedCount"]

            writer.writerow([user, content, likes])

    print("Comments saved to data/comments.csv")

if __name__ == "__main__":
    song_name = input("Enter song name: ")

    song_id = search_song(song_name)
    print("Song ID:", song_id)

    if song_id:
        comments = get_comments(song_id)
        print("Number of comments:", len(comments))

        save_comments(comments)