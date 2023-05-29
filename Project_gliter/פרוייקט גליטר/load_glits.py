import requests
import headers
import login
import datetime

HEADERS = headers.get_headers()
HEADERS.update({"If-None-Match": 'W/"1af-F6nwmJkzc8IAMTkXKekmhfBQf1w"'})

def change_load_msg(url):
    LOGIN_DATA = login.login_data()
    HEADERS["Cookie"] = LOGIN_DATA[1]
    resp = requests.get(url, headers=HEADERS)
    if "Server Failure" in resp.text:
    	print("make sure you entered a valid feed id")
    else:
    	print("the program did what you asked for")


def load_another_feed():
    x = input("Enter someone else's feed id: ")
    url = f'http://cyber.glitter.org.il/glits?feedOwnerId={x}&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&count=2'
    change_load_msg(url)


def more_glits_one_load():
	x = 'one'

	while True:
		try:
			int(x)
			break;
		except ValueError:
			while x < '0' or x > '5':
				x = input("Enter how much glits to load(0 - 5): ")

	url = f'http://cyber.glitter.org.il/glits?feedOwnerId=8269&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&count={x}'
	change_load_msg(url)