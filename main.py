from pytube import YouTube
myStream = YouTube("https://www.youtube.com/watch?v=ZiKMIuYidY0").streams.get_by_itag('18')#Add the video link here in YouTube function
myStream.download("Music/")#folder name where you want to save the video
