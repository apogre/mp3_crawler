import MySQLdb
import urllib
from mutagen.mp3 import MP3
from get_tags import *
from partial_d import *
from hurry.filesize import size
import datetime

class MySQLStorePipeline(object):

	def __init__(self):
		self.conn = MySQLdb.connect(
			host = '127.0.0.1',
			db = 'testdb_mp3',
			user ='root',
			passwd = 'root',
			charset = 'utf8',
			use_unicode = True
		)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):

		try:
			for link in item['link']:
				get_file(link)
				tags, bitrate = get_tags()
				fsize = Downloader()
				file_size = fsize.getContentLength(link)
				length = (file_size*8)/bitrate
				file_size = size(file_size)
				bitrate = bitrate/1000
				length = round(length)
				length = str(datetime.timedelta(seconds=length))
				
				year = genre = comment =track = artist=album=songtitle="unavailable"



				keys= tags.keys()
				for key in keys:
					if key == 'TALB':
						album = tags['TALB']
					elif key == 'TPE1':
						artist = tags['TPE1']
					elif key == 'TIT2':
						songtitle = tags["TIT2"]
					elif key == 'TDRC':
						year = tags['TDRC']
					elif key == 'TCON':
						genre=tags['TCON']
					elif key == 'COMM':
						comment = tags['COMM']
					elif key == 'TRCK':
						track = tags['TRCK']
					else:
						pass


				self.cursor.execute("insert into files(link,artist,album,songtitle,year,genre,comment,track,bitrate,size,length) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(link,artist,album,songtitle,year,genre,comment,track,bitrate,file_size,length))		
				self.conn.commit()
				with open("link_exec.txt", "a") as f:
					f.write("%s \n" % (self.cursor._last_executed)) 
			
		except MySQLdb.Error as e:
			with open("error.txt", "a") as f:
				f.write("%s %s \n" % (item['link'],e)) 

		return item
		