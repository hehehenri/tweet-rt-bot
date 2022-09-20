import tweepy
import schedule
import time
import datetime
import os


CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'key'
ACCESS_TOKEN = 'key'
ACCESS_TOKEN_SECRET = 'key'


RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


def cls():
	os.system('cls')

cls()


def login():

	print((RED + "Logando "), end="\r")
	time.sleep(0.5)
	print((RED + "Logando ."), end="\r")
	time.sleep(0.5)
	print((RED + "Logando .."), end="\r")
	time.sleep(0.5)
	print((RED + "Logando ..."), end="\r")
	time.sleep(0.5)	


try:
	login()
	cls()
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	print(BLUE + "Logado!")
	time.sleep(1)	
except:
	print(RED + "Erro no Login!")


api = tweepy.API(auth)


data = (datetime.datetime.now().strftime("%H:%M"))


def rt():
	for result in api.search(q="#bolhadev", count=30):
		try:
			api.retweet(result.id)
			print("\n")
			print(BLUE + data + " " + GREEN + result.text)

		except:
			time.sleep(1)		

schedule.every(1).seconds.do(rt)

while 1:
	schedule.run_pending()
	time.sleep(1)
