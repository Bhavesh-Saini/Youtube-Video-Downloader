from pytube import Playlist
link=input("Enter url of playlist to download: ")
pl=Playlist(link)
print(f'Playlist Title: {pl.title}')
print('Number of videos in playlist: %s'%len(pl.video_urls))
# downloading every video in 720p
print("Your videos are downloading, please wait for sometime...")
for video in pl.videos:
    video.streams.filter(res="720p").first().download()
print("Playlist downloaded,check in the folder")



# # giving quality option for every video to download
# for video in pl.videos:
#     videos=video.streams.all()
#     opt=list(enumerate(videos))
#     for i in opt:
#          print(i)

#     print()
#     strm=int(input("Choose option: "))
#     videos[strm].download()
# print("Playlist downloaded,check in the folder")
