
from pytube import YouTube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLbu_fGT0MPsv9W38hFS_mTYbdOUOnidzG")

links=[]
for url in playlist:
	links.append(url)

for link in links:  
    yt = YouTube(link)
    print(yt)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    try:
    	stream.download()
    	print("Downloaded: ", link)
    
    except:
    	print("some error occured")