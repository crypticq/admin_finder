import requests
from time import sleep
import warnings
import argparse
import concurrent.futures
from bs4 import BeautifulSoup
from time import time
from pyfiglet import figlet_format
from termcolor import colored

warnings.filterwarnings('ignore', message='Unverified HTTPS request')



class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



print((colored(figlet_format("By Eng Yazeed"), color="red")))





headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:78.0) Gecko/20100101 Firefox/78.0',
}







def quick_check(url):
    r = requests.get(url , headers=headers , verify=False)
    soup = BeautifulSoup(r.text , 'lxml')
    if soup is not None:
        return soup.title.text



t1 = time()


def buster(site):
    try:


        r = requests.get(site , headers=headers, verify=False)

        http = r.status_code

        if http != 404:

            print (style.CYAN , '[*] {0} |  {1}  | title is {2} [*]'.format(r.url,r.status_code,quick_check(r.url)))
           

        # print('Not found' , pip)
        else:
            print(style.RED , r.status_code + "|" , r.url)

    except Exception:

        pass





def get_args():
    parser = argparse.ArgumentParser(description=' admin page Discovery ..')
    parser.add_argument('-u', '--url', dest="url", required=True, action='store', help='Url')
    parser.add_argument('-f', '--file', dest="fileinput", required=True, action='store', help=' list for Discovery. ')
    parser.add_argument('-t', '--threads', dest="threads", required=True, type=int ,  action='store', help=' list for Discovery. ')
    args = parser.parse_args()
    return args



if __name__ == '__main__':

    args = get_args()
    url = args.url
    files = args.fileinput
    thread = args.threads
    idk = []
    if not url.startswith('http') or url.startswith('https'):
        url = 'http://' + url

    if url.endswith('/'):
        url = url.strip('/')
    wordf = open(files, 'r').read().splitlines()


    for paths in wordf:
        ik = paths.strip()
        to = url+"/"+ik
        idk.append(to)
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as pool:
        pool.map(buster,idk )

t2 = time()

elapsed = t2 - t1

print(style.GREEN, 'time took to Complete %f seconds.' % elapsed)






