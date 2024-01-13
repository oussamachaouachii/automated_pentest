#!/bin/python3
import requests,re,os,sys

session = requests.Session()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
#terminal_size = os.get_terminal_size().columns

try:
    from colorama import init
    init()
    R = '\033[0;31m'
    G = '\033[0;32m'
    B = '\033[0;34m'
    LR = '\033[1;31m'
    LC = '\033[1;36m'
except:
    pass
    R = ''
    G = ''
    B = ''
    LR = ''
    LC = ''


def checkRobots(url):
	r = session.get(url+'robots.txt', verify=False, headers=header)
	if r.status_code == requests.codes.ok:
		lines = r.text.splitlines()
		print(f'<h3>Checking for the existence of robots.txt and its content</h3>')
		print(f'</br> robots.txt Found Checking ')
		if re.search('admin|api|controll_panel|users|usarios|administrator|json|login|php|uploads|manager|dev|FCKEditor|old|db|private|members', r.text):
			for keyword in lines:
				if re.search('admin|api|controll_panel|users|usarios|administrator|json|login|php|uploads|manager|dev|FCKEditor|old|db|private|members', keyword):
					print(f'</br> Found {keyword}')
				else:
					pass
		else:
			print(f'</br> No interesting files found in robots.txt </br>')
	else:
		print(f'</br> Robots.txt was not found. </br>')

url=sys.argv[1]
url=url+"/"
checkRobots(url)
