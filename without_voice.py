import os, datetime, random
from moviepy.editor import VideoFileClip
import time

klasor = os.listdir("original_videos")

for dosya in klasor:
    try:

        ran = random.randrange(10**20)
        myhex = "%05x" % ran
        date1 = datetime.datetime.now()

        videoclip = VideoFileClip("original_videos" + os.sep + dosya)
        new_clip = videoclip.without_audio()
        new_clip.write_videofile("without_files" + os.sep + str(date1.hour) + str(date1.minute) + str(date1.day) + str(date1.month) + str(date1.year) + str(myhex) + "_" + dosya)
        time.sleep(5)
        os.remove("original_videos" + os.sep + dosya)
        time.sleep(5)
    except:
        continue