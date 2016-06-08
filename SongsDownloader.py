import urllib
import json as m_json
from google import search
import subprocess

songsfile= open('songs.txt','r')

with open('songs.txt', 'r') as songsfile:
	    mySongsList= songsfile.read().splitlines()
mysonglistURL=[]
for line in mySongsList:
    query= str(line+r" site:youtube.com")
    print query,
    for url in search(query, num=1, stop=1):
        mysonglistURL.append(url)
        print url

print "\n--++==List of URLs==++--\n"
for line in mysonglistURL:
    print str(line)

for line in mysonglistURL:
    print "\nDownloading: "+line
    process_call= "youtube-dl -x --audio-format mp3 --yes-playlist --audio-quality 0 "+line
    try:
        print subprocess.check_output(["youtube-dl", "-o", "./DownloadedSongs/%(title)s.%(ext)s", "-x", "--audio-format", "mp3", "--yes-playlist", "--audio-quality", "0", line])
    except subprocess.CalledProcessError, e:
        print "Ping stdout output:\n", e.output
    print "\nFinished Download: "+line