from pytube import YouTube
link=input("Enter url of youtube video to download: ")
# this  variable stores all information of youtube video
video=YouTube(link)
print("Video Title: ",video.title)
# video quality options in all format mp4/mp3
videos=video.streams.all()

# # only audio downloading options are given
# videos=video.streams.filter(only_audio=True)

opt=list(enumerate(videos))
for i in opt:
    print(i)

print()
strm=int(input("Choose option: "))
print("Video downloading, please wait for sometime...")
videos[strm].download()
print("Video downloaded successfully, check in the folder")