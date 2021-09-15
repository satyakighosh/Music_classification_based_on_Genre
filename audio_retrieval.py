import youtube_dl
import re
import os
from tqdm import tqdm
import pandas as pd
import numpy as np



WAV_DIR = '/content/drive/MyDrive/IIT_Guwahati/IITG_DigitalSignalProcessorsLab/Music_classification_by_Genre/wav_files/'
genre_dict = {
            '/m/064t9': 'Pop_music',
            '/m/0glt670': 'Hip_hop_music',
            '/m/06by7': 'Rock_music',
            '/m/06j6l': 'Rhythm_blues',
            '/m/06cqb': 'Reggae',
            '/m/0y4f8': 'Vocal',
            '/m/07gxw': 'Techno',
            }

genre_set = set(genre_dict.keys())



temp_str = []
with open('/content/drive/MyDrive/IIT_Guwahati/IITG_DigitalSignalProcessorsLab/Music_classification_by_Genre/data-files/csv_files/unbalanced_train_segments.csv', 'r') as f:
    temp_str = f.readlines()

N=400000   # how many audio files to check for the above genres
temp_str=temp_str[0:N]


data = np.ones(shape=(1,4)) 
for line in tqdm(temp_str):
    line = re.sub('\s?"', '', line.strip())
    elements = line.split(',')
    common_elements = list(genre_set.intersection(elements[3:]))
    if  common_elements != []:
        data = np.vstack([data, np.array(elements[:3]
                                         + [genre_dict[common_elements[0]]]).reshape(1, 4)])

df = pd.DataFrame(data[1:], columns=['url', 'start_time', 'end_time', 'class_label'])
df.to_csv('/content/drive/MyDrive/IIT_Guwahati/IITG_DigitalSignalProcessorsLab/Music_classification_by_Genre/music_list.csv',index=False)



df['start_time'] = df['start_time'].map(lambda x: np.int32(np.float(x)))
df['end_time'] = df['end_time'].map(lambda x: np.int32(np.float(x)))

for i, row in tqdm(df.iterrows()):
    url = "'https://www.youtube.com/embed/" + row['url'] + "'"
    file_name = str(i)+"_"+row['class_label']
    
    try:
        command_1 = "ffmpeg -ss " + str(row['start_time']) + " -i $(youtube-dl -f 140 --get-url " +  url + ") -t 10 -c:v copy -c:a copy " + file_name + ".mp4"

        command_2 = "ffmpeg -i "+ file_name +".mp4 -vn -acodec pcm_s16le -ar 44100 -ac 1 " + WAV_DIR + file_name + ".wav"

        command_3 = 'rm ' + file_name + '.mp4' 

        # Run the 3 commands
        os.system(command_1 + ';' + command_2 + ';' + command_3 + ';')
    
    except:
        print(i, url)
        pass

