import os
import time

drums = {'Kick': []}
         # 'Closed Hat': [], 'Open Hat': [], 'Snare': [], '808': [], 'Sub': [], 'Crash': [], 'Shaker': [],
         # 'Cymbal': [], 'Clap': [], 'Snap': [], 'FX': [], 'Chant': [], 'Perc': []}
kicks = []
closed_hats = []
open_hats = []
snares = []
bass = []
crashes = []
shakers = []
cymbals = []
claps_snaps = []
fx = []
chants = []
percussion = []

directory = '/Users/jibraansiddiqi/Music/SamplesPacks copy'
counter = 0
for filename in os.listdir(directory):
    for k, v in drums.items():
        print(k, v)
    pack_name = os.path.join(directory, filename)
    for file in os.listdir(pack_name):
        if '.wav' in file:
            for shot in drums.keys():
                if shot.lower() in file.lower():
                    if len(drums[shot]) > 0:
                        for key in drums[shot]:
                            if filename in key:
                                index = drums[shot].index(key)
                                try:
                                    drums[shot][index][filename].append(file)
                                except KeyError:
                                    drums[shot].append({filename: [file]})
                            else:
                                drums[shot].append({filename: [file]})
                    else:
                        drums[shot].append({filename: [file]})
