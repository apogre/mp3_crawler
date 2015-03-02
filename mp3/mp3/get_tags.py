from mutagen.mp3 import MP3
import mutagen
from partial_d import *

def get_file(url):
	num_streams = 1000
	dest_fname = "filepart0.mp3"
	dman = Downloader()
	dman.downloadFile(url, num_streams, dest_fname)

	
def get_tags():
	try:
		tags = mutagen.File('filepart0.mp3')
		audio = MP3("filepart0.mp3")
		print tags
		bitrate= audio.info.bitrate
		
		return tags,bitrate
		
	except mutagen.id3.error:
	    print 'id3 error'
