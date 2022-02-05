#!/usr/bin/env python3

import csv
import os

input_file = './sounds.csv'
output_directory = './output'

try:
    filereader = csv.reader(open(input_file), delimiter=",")
except:
    print('Error opening file {}'.format(input_file))
    exit()

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

next(filereader, None) # skip headers

for filename, text in filereader:
    print(filename)
    path = os.path.join(output_directory, filename)
    try:
      os.remove(path)
    except IOError:
      print('.')

    # Do whatever you want here to generate your voice files
    os.system("say -v Moira -o {}.aiff {}".format(path, text))
    os.system("ffmpeg -hide_banner -loglevel panic -i {0}.aiff {0}".format(path))
    os.remove("{}.aiff".format(path))
