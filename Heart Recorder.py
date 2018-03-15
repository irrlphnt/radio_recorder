#! /usr/bin/python

import requests
import time
import os
import shutil

stream_url = input("Paste the address of the stream you want to record here:\n")

r = requests.get(stream_url, stream=True)
timestr = time.strftime("%d%m%Y-%H-%M")
file_name = input("Type in the name of the radio station:\n") + timestr + ".mp3"
recording_time = input("How many seconds would you like to record for?")# How long to record for, in seconds
start_time = time.time()
end_time = start_time + recording_time
print(recording_time / 60)

with open("/Users/pwilcox/Desktop/HeartFM/" + file_name, 'wb') as f:
    try:
        print("Recording " + str(recording_time/60) + " minutes of HeartFM...\nPresss ctrl + c to stop")
        for block in r.iter_content(1024):
            f.write(block)
            if time.time() > end_time:
                f.close()
        	#Copy the file
        	shutil.copy("/Users/admin/Desktop/KerryMoore/" + file_name, "/Volumes/shared/Radio Recording/" + file_name)
        	quit()
    except KeyboardInterrupt:
        pass