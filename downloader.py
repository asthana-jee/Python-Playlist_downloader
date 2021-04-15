
from pytube import YouTube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLbu_fGT0MPsv9W38hFS_mTYbdOUOnidzG") #Edit this playlist with your playlist link

links=[] 		
#Created a list to store links 
for url in playlist:      
	#This loop runs throughout the playlist to store every video's url
	links.append(url)

for link in links:  	  
    #Download video one by one
    yt = YouTube(link)
    print(yt)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    #Determines the quality of video

    try:
    	stream.download()
    	print("Downloaded: ", link)
    
    except:
    	print("some error occured")
