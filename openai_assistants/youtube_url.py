from googleapiclient.discovery import build

from decouple import config

api_key = config("google_key")
youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PLu5PUxcrztwXGRgj9D658_K25K7KgTXQ5'
playlist_items = []

next_page_token = None
while True:
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,        
        pageToken=next_page_token
    )
    response = request.execute()

    for item in response['items']:
        video_id = item['contentDetails']['videoId']
        playlist_items.append(f'https://www.youtube.com/watch?v={video_id}')

    next_page_token = response.get('nextPageToken')

    if not next_page_token:
        break


print(len(playlist_items))

#for video_url in playlist_items:
#    print(video_url)