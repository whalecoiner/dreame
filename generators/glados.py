import requests
import csv
from pydub import AudioSegment
import os
import tarfile

audio_dir = "../audio/"
voicepack_dir = "../voicepacks/"

if not os.path.exists(audio_dir):
  os.mkdir(audio_dir)

if not os.path.exists(voicepack_dir):
  os.mkdir(voicepack_dir)

# Glados
files = []
output_dir = os.path.join(audio_dir, "glados")
print(output_dir)
if not os.path.exists(output_dir):
  os.mkdir(output_dir)
with open('../sounds.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, quotechar='"')
  next(reader, None) # Skip CSV header
  for row in reader:
    print(row[0], row[2])
    input_file = os.path.join(output_dir, f"{row[0]}.wav")
    output_file = os.path.join(output_dir, f"{row[0]}.ogg")
    glados_params_arg = {'text': row[2]}
    glados_url = 'https://glados.c-net.org/generate'
    resp_get = requests.get( glados_url, params=glados_params_arg)
    with open(input_file, "wb") as f:
      f.write(resp_get.content)
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="ogg")
    os.remove(input_file) 
    files.append(os.path.abspath(output_file))

tar = tarfile.open("../voicepacks/glados_voice_pack.tar.gz", "w:gz")
for file in files:
  tar.add(file)
tar.close()
