#This lab asks ChatGPT for subjects discussed in a vide and asks for the time code.

from youtube_transcript_api import YouTubeTranscriptApi
import openai

openai.api_key = 'APIKEY'

url = 'https://www.youtube.com/watch?v=UCGaKvZpJYc'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "You are a database computer"},
    {"role": "assistant", "content": "data is stored in JSON {text:'', start:'', duration:''}"},
    {"role": "assistant", "content": str(transcript)},
    {"role": "user", "content": "what are the topics discussed in this video. Provide start time codes in seconds and also in minutes and seconds"}
  ]
)
timecode = response["choices"][0]["message"]["content"]

print(timecode)
