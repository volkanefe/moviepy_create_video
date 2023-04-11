import os, time, random
from moviepy.editor import *


video_yol = os.listdir("without_files")
ses_yol = os.listdir("facebook_mp3")




for dosya in video_yol:
      # print(dosya)
      # print("------")
      # time.sleep(2)
      try:
            videoclip = VideoFileClip("without_files" + os.sep + dosya)
            audioclip = AudioFileClip("facebook_mp3" + os.sep + random.choice(ses_yol))

            new_audioclip = CompositeAudioClip([audioclip]).set_duration(videoclip.duration)
            videoclip.audio = new_audioclip
            

            logo = (ImageClip("logo.png")
                  .set_duration(videoclip.duration)
                  .resize(height=100) # if you need to resize...
                  .margin(right=10, top=10, opacity=0) # (optional) logo-border padding
                  .set_pos(("right","top")))
      
            final_video = CompositeVideoClip([videoclip, logo])
            

            final_video.write_videofile("fb_join_files" + os.sep + dosya)
            time.sleep(10)
            os.remove("without_files" + os.sep + dosya)
            time.sleep(3)
      except:
            continue
      