
from threading import Thread
import threading
import requests
from time import sleep,perf_counter
import warnings
import argparse
from bs4 import BeautifulSoup





warnings.filterwarnings('ignore', message='Unverified HTTPS request')



start_time = perf_counter()       


def banner():
	print('#' * 31)
	print('Coded By Eng Yazeed')
	print('#' * 31)



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:78.0) Gecko/20100101 Firefox/78.0',
}



def check_proxy(site,pip):
	try:
		global founds

		founds = []

		r = requests.get('{}/{}'.format(site,pip) , headers=headers , verify=False)
		
		http = r.status_code 

		if http == 200:

			print ('  \033[1;32m[+]\033[0m path found: %s'% r.url)
			founds.append(r.url)
		elif http == 404:

			print ('  \033[1;31m[-]\033[1;m %s'% r.url)

		elif http == 302:

			print ('  \033[1;32m[+]\033[0m Potential EAR vulnerability found : ' + r.url)
			founds.append(r.url)


		elif http > 500:
			pass

		else:
			print ('  \033[1;31m[-]\033[1;m %s'% r.url)
			founds.append(r.url)
			
			# print('Not found' , pip)

	except Exception:
		
		pass




def get_args():
	parser = argparse.ArgumentParser(description=' admin page Discovery ..')
	parser.add_argument('-u', '--url', dest="url", required=True, action='store', help='Url')
	parser.add_argument('-f', '--file', dest="fileinput", required=True, action='store', help=' list for Discovery. ')
	args = parser.parse_args()
	return args

args = get_args()
url = args.url
files = args.fileinput



if __name__ == '__main__':
	if not url.startswith('http') or url.startswith('https'):
		url = 'http://' + url
	
	if url.endswith('/'):
		url = url.strip('/')
	wordf = open(files , 'r').read().splitlines()
	threads = []

	for paths in wordf:
		#for paths in wordf:

	    thread = Thread( target=check_proxy, args=(url,paths.strip(),))
	    thread.start()
	    threads.append(thread)

	for thread in threads:
		thread.join()




	

	print("\033c", end="")
	banner()

	for found in founds:
		#print('Found Total of {} links'.format(len(founds)))
		print(found)
		r = requests.get(found , headers=headers)
		soup = BeautifulSoup(r.content , 'lxml')
		try:
			print('this url {} has the title of {}'.format(found,soup.title.text))
		except:
			pass

	end_time = perf_counter()
	print('Found Total of {} links might by intersting paths check them . '.format(len(founds)))
	print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

	
