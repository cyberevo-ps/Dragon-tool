import os
os.system("clear")
from pytube import YouTube
print ("""\033[0;31m
         __  __         ______     __
         \ \/ /__  __ _/_  __/_ __/ /  ___
          \  / _ \/ // // / / // / _ \/ -_)
          /_/\___/\_,_//_/ _\_,_/_.__/\__/__
         / _ \___ _    __/ /__  ___  ___/ /__ ____
        / // / _ \ |/|/ / / _ \/ _ \/ _  / -_) __/
       /____/\___/__,__/_/\___/_//_/\_,_/\__/_/



            Install The vidios Youtube 
          in Termux By bo Haydar El mo3alem
""")
def download_video(url):
    youtube_video = YouTube(url)
    video_stream = youtube_video.streams.get_highest_resolution()
    video_stream.download('/sdcard/Download')  # قم بتغيير المسار إلى المجلد الذي ترغب في حفظ الفيديو فيه
    print("\033[1;31mThe video has been uploaded successfully!! video track :/sdcard/Download")

# مرحبًا بك
print("\033[1;31mENTER THS LINK VIDEO ==> :\033[1;32m")
video_url = input()

# استدعاء الدالة لتنزيل الفيديو
download_video(video_url)
