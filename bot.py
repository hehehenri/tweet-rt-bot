import tweepy
import schedule
import time
import datetime
import os


CONSUMER_KEY = '3QEvLzP9fkO9xLuehFuulkRYG'
CONSUMER_SECRET = 'EDH8GvpoZ30IpUK9oe2EpDNnzd4ah5H3UZhFIpwRl4mWArVwsW'
ACCESS_TOKEN = '778442768188182528-Xl36GqdZW55EgFvCGkMCOLrDT2oiK52'
ACCESS_TOKEN_SECRET = 'j9P36rI9UOylgrGcTbLm7U0NN60gvxjmI2xAmlyXCpuOy'


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
	for result in api.search(q="maicon kuster", count=30):
		try:
			api.retweet(result.id)
			print("\n")
			print(BLUE + data + " " + GREEN + result.text)

		except:
			time.sleep(1)

	for result in api.search(q="maicon küster", count=30):
		try:
			api.retweet(result.id)
			print("\n")
			print(BLUE + data + " " + GREEN + result.text)

		except:
			time.sleep(1)

	for result in api.search(q="my conquister", count=30):
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