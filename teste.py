# from googleapiclient.discovery import build
# from youtube_transcript_api import YouTubeTranscriptApi
# from dotenv import load_dotenv,find_dotenv
# import os
# import sqlite3

# #setting sqlite3 database
# teste_db = "teste.db"
# prod_db = "prod.db"

# con = sqlite3.connect(prod_db)

# cur = con.cursor()

# load_dotenv(find_dotenv())

# # Set up OAuth 2.0 credentials
# API_KEY = os.getenv("API_KEY")

# youtube = build('youtube','v3',developerKey=API_KEY)

# maxResults = 10
# # Search for videos in the specified genre
# search_response = youtube.search().list(
#     q='games',
#     part='id',
#     maxResults=maxResults,  # Adjust the number of search results as needed
#     type='video',
#     regionCode='US',
#     order='searchSortUnspecified'
# ).execute()

# video_ids = [item['id']['videoId'] for item in search_response['items']]

# for video_id in video_ids:
#     video_response = youtube.videos().list(
#         part='snippet',
#         id=video_id
#     ).execute()
#     tags = video_response['items'][0]['snippet']['title']
#     print(tags)
    