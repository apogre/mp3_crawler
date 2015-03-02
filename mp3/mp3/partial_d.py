import urllib2
from threading import Thread
  
class Downloader:
    def __init__(self):
        pass
  
    def downloadFile(self, url, num_streams, dest_fname):
        file_size = self.getContentLength(url)
        print file_size
  
        if not self.supportsPartialContent(url):
            print "The server doesn't support partial content!! Resuming with Single Stream"
            self.downloadStream(url, dest_fname, "bytes=0-"+`file_size`)
            return
  
        initial = 0
        block   = int(file_size / num_streams)
        final   = 5000
        files   = []
        threads = []
  
        for i in xrange(1):
            drange  = "bytes=" + `initial` + "-" + `final`
            print drange
            files.append("filepart" + `i`+".mp3")
              
            t = Thread(target=self.downloadStream, args=(url, files[i], drange))
            threads.append(t)
              
            # initial = final
            # final   = (final + block) if (i < num_streams-2) else file_size
  
        [t.start()  for t in threads]
        [t.join()   for t in threads]
        
  
        # self.concatFiles(files, dest_fname);
          
  
    def concatFiles(self, original, dest):
        final_file = open(dest, 'wb')
        for f in original:
            fopener = open(f, 'rb')
            final_file.write(fopener.read())
            fopener.close()
        final_file.close()
        return
  
    def supportsPartialContent(self, url):
        request = urllib2.Request(url)
        request.add_header("Range", "bytes=0-10")
        opener  = urllib2.urlopen(request)
        print opener.getcode()
        return True if opener.getcode() == 206 else False
  
    def downloadStream(self, url, file_name, range):
        request = urllib2.Request(url)
        request.add_header("Range", range)
        opener  = urllib2.urlopen(request)
  
        f = open(file_name, "wb")
        f.write(opener.read())
        f.close()
  
    def getContentLength(self, url):
        content = urllib2.urlopen(url)
        meta = content.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        return file_size
  
  
# url = "http://uhmp3.com/user-mp3-to/8-apa-salahku-dmasiv.mp3"
# num_streams = 1000
# dest_fname = "testfile.mp3"
# dman = Downloader()
# dman.downloadFile(url, num_streams, dest_fname)
# # dman.downloadStream(url,dest_fname,1024)