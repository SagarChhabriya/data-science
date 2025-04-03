import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()   

# Retrieve API key from environment variables
api_key = os.getenv('YOUTUBE_API_KEY')
if not api_key:
    raise ValueError("Missing API key. Set YOUTUBE_API_KEY in the .env file or environment variables.")

youtube = build('youtube', 'v3', developerKey=api_key)

# Replace with your playlist ID
playlist_id = 'PL5OhSdfH4uDsyUM02ZHl2mOYBpihCYsml'

def get_video_links(youtube, playlist_id):
    video_links = []
    next_page_token = None

    while True:
        playlist_items = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in playlist_items['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_links.append(f'https://www.youtube.com/watch?v={video_id}')

        next_page_token = playlist_items.get('nextPageToken')
        if not next_page_token:
            break

    return video_links

video_links = get_video_links(youtube, playlist_id)

# Print all the video links
for link in video_links:
    print(link)
