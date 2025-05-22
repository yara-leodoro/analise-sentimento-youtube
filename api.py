import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
from sentiments import classificar_sentimento

load_dotenv()

api_key =  os.getenv("API_KEY")  # Substitua pela sua chave de API do YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

video_id = os.getenv("VIDEO_ID")  # Substitua pelo ID do vídeo que você deseja analisar
max_comments = 50

video_info = youtube.videos().list(part="snippet", id=video_id).execute()
video_snippet = video_info["items"][0]["snippet"]
titulo_video = video_snippet["title"]
nome_canal = video_snippet["channelTitle"]

comments = []
next_page_token = None

while len(comments) < max_comments:
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token,
        textFormat="plainText"
    ).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        if len(comments) >= max_comments:
            break

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

resultados = classificar_sentimento(comments)

for r in resultados:
    r["Canal"] = nome_canal
    r["Titulo do Vídeo"] = titulo_video

df = pd.DataFrame(resultados)
df = df[df["Sentimento"] != "Erro"]
path = os.getenv("OUTPUT_PATH") + "/"
df.to_csv(path + "comentarios_analisados.csv", index=False)

print("Arquivo 'comentarios_analisados.csv' salvo com sucesso!")
