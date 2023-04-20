import openai
import requests
import os

os.system("clear")

openai.api_key = "your-api-key"

def ask_chatgpt(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt},
    ]
  )
  
  return response.choices[0].message["content"]

while True:
  os.system("rec input.mp3")

  audio_file = open("input.mp3", "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)["text"]

  if transcript.lower() != "stop.":
    response = ask_chatgpt(transcript)
  else:
    break

  os.system("rm input.mp3")

  headers = {
    'accept': 'audio/mpeg',
    'xi-api-key': "your-api-key",
    'Content-Type': 'application/json',
  }

  json_data = {
    'text': response,
  }

  response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB', headers=headers, json=json_data)

  with open('prompt_response.mp3', 'wb') as f:
    f.write(response.content)

  os.system("afplay prompt_response.mp3")
  os.system("clear")
  continue
