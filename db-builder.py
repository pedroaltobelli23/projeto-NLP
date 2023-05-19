from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv,find_dotenv
import os
import sqlite3

#setting sqlite3 database
teste_db = "teste.db"
prod_db = "prod.db"

con = sqlite3.connect(prod_db)

cur = con.cursor()

load_dotenv(find_dotenv())

# Set up OAuth 2.0 credentials
API_KEY = os.getenv("API_KEY")

youtube = build('youtube','v3',developerKey=API_KEY)

maxResults = 2000
# Search for videos in the specified genre
search_response = youtube.search().list(
    q='games',
    part='id',
    maxResults=maxResults,  # Adjust the number of search results as needed
    type='video',
    regionCode='US'
).execute()

# Extract the video IDs from the search results
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Fetch the tags for each video
total = 0
failed = 0
for video_id in video_ids:
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ""
        for subtitle in transcript:
            text+=" " + subtitle['text']
        tags = video_response['items'][0]['snippet']['tags']
        title = video_response['items'][0]['snippet']['title']
        tags_str = " , ".join(tags)
        total+=1
        print(f"data from: {video_id} added.{total}/{maxResults-failed}")
        cur.execute(f'''
        INSERT INTO videos (video_id,title,tags,transcript) values(?,?,?,?)       
        ''',(video_id,title,tags_str,text))
        con.commit()
    except:
        print("Algo deu errado. Video nao possui legendas ou tags ou ja existe no database")
        failed+=1
        continue


con.close()