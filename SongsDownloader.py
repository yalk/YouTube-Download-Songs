import urllib
import json as m_json
from google import search
import subprocess

songsfile= open('songs.txt','r')

with open('songs.txt', 'r') as songsfile:
    mySongsList= songsfile.read().splitlines()
    totalSongs=len(mySongsList)
i=1
songsListMapper=[]

print "YouTube Song Downloader v1.2"

for line in mySongsList:

    query= str(line+r" site:youtube.com")
    print "\n\nTitle: "+line

    for url in search(query, num=1, stop=1):

        print "URL: "+url+"\n\nDownloading..."
        
        try:
            print subprocess.check_output(["youtube-dl", "-o", "./DownloadedSongs/%(title)s.%(ext)s", "-x", "--audio-format", "mp3", "--yes-playlist", "--audio-quality", "0", url])

        except subprocess.CalledProcessError, e:
            print "Ping stdout output:\n", e.output

        print "Download Complete!"
        currentMap=[line,url]
        songsListMapper.append(currentMap)
    i=i+1

SongURLListFile= open("songLinks.txt","wb")
for line in songsListMapper:
    SongURLListFile.write(line[0]+","+line[1]+"\n")
SongURLListFile.close()

SongURLListFile= open("songLinks.txt","r")
print "\n\n--++==Final URL List==++--\n"+str(SongURLListFile.read())