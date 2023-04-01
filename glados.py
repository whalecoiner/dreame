import requests
import csv
from pydub import AudioSegment
import os

# Download sentence list.
csv_get = requests.get('https://github.com/whalecoiner/dreame/raw/main/sounds.csv')
with open("./sounds.csv", "wb") as f:
  f.write(csv_get.content)

# Glados
os.mkdir("audio/glados")
with open('sounds.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, quotechar='"')
  next(reader, None) # Skip CSV header
  for row in reader:
    print(row[0], row[2])
    glados_params_arg = {'text': row[2]}
    glados_url = 'https://glados.c-net.org/generate'
    resp_get = requests.get( glados_url, params=glados_params_arg)
    with open("audio/glados/" + row[0] + ".wav", "wb") as f:
      f.write(resp_get.content)
    audio = AudioSegment.from_wav("audio/glados/" + row[0] + ".wav")
    audio.export("audio/glados/" + row[0] + ".ogg", format="ogg")
    os.remove("audio/glados/" + row[0] + ".wav") 
