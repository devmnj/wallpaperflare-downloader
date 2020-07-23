from wallspyder import flareDownloader
import threading

t1 = threading.Thread(target=flareDownloader('code').download(30))
t2 = threading.Thread(target=flareDownloader('suse').download(20))
t3 = threading.Thread(target=flareDownloader('puzzle').download(delay=10))
t1.start()
t2.start()
t3.start()
