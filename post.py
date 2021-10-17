import os

import requests

from instabot import Bot

from PIL import Image, ImageDraw, ImageFont

import glob

import sys

try:

	types = sys.argv[1]
	
except IndexError:

	print('''python3 main.py [OPTION]

options:
		
		-q quotes: to post random quotes
		
		-j jokes: to post some random jokes
		
		-i to post some ideas

enjoy! (':''')

	exit()

def post(content):

	bot = Bot()

	cookie_del = glob.glob("config/*cookie.json")

	try:

		os.remove(cookie_del[0])
	
	except IndexError:
		
		pass

	bot.login(username = "USERNAME", password = "PASSWORD")
	
	os.system("rm post.jpeg")
	
	posted(content)
	
	nn = open('post.txt', 'r').read()
	
	desc = ''.join([f"#{word} " for word in content.split()])
	
	desc = f'#{nn} {desc}'
	
	bot.upload_photo("post.jpeg", caption = f"{desc}")
	
	fnn = int(nn) + 1
	
	os.system(f"echo '{fnn}' > post.txt")

def start():

	if types == "quotes" or "-q":

		request = requests.get('https://api.quotable.io/random', auth=('user', 'pass'))
		
		quotes = request.json()
		
		n = quotes['content']
	
	elif types == "jokes" or "-j":
	
		request = requests.get('https://usefull-api.herokuapp.com/joke/', auth=('user', 'pass'))
		
		jokes = request.json()
		
		n = jokes['joke']
		
	elif types == "ideas" or "-i":
		
		request = requests.get('https://usefull-api.herokuapp.com/idea', auth=('user', 'pass'))
		
		ideas = request.json()
		
		n = ideas['idea']
	
	else:
	
		print('''python3 main.py [OPTION]

options:
		
		-q quotes: to post random quotes
		
		-j jokes: to post some random jokes
		
		-i to post some ideas

enjoy! (':''')
	
	post(n)
	
	start()
	
def posted(text):
	
	img = Image.new('RGB', (100, 30), color = 'black')
	
	newsize = (1080, 608) 
	
	img = img.resize(newsize)

	fnt = ImageFont.truetype('NotoSans/NotoSans-Regular.ttf', 30)

	d = ImageDraw.Draw(img)
	
	'''
	
	if ',' in text:
	
		text = ''.join([f'{itemss}\n' for itemss in text.split(',')])
		
	else:
		
		text = ''.join([f'{itemss}\n' for itemss in text.split('.')])
		
	'''
	
	numm = 0
	
	idk = []
	
	for words in text.split():
	
		idk.append(words)
		
		idk.append(" ")
		
		if int(numm) == 11:
		
			idk.append("\n")
		
		numm = numm + 1
		
	text = ''.join([bruh for bruh in idk])

	d.text((135,304), f'{text}\n\n                                 -NacreousDawn596', font=fnt, fill=(255, 255, 255))

	img.save('post.jpeg', 'JPEG')

start()
