
from threading import Thread
import requests



def Check_me(site,pip):
	try:
		r = requests.get('{}/{}'.format(site,pip))
		if r.status_code < 300 or r.status_code == 200:
			print('Found' , r.url)
	except Exception as e:
		pass


wordf = open('/usr/share/seclists/Discovery/Web-Content/common.txt' , 'r').read().splitlines()
threads = []
site = 'http://testphp.vulnweb.com'


for paths in wordf:
    thread = Thread( target=Check_me, args=(site,paths.strip(),))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
