import requests
import headers
from json import load

HEADER = headers.login_headers()
USER_DATA = ''
URL = "http://cyber.glitter.org.il/user/"

def login():
	global USER_DATA
	user_name = input("Enter your user name: ")
	password = input("Enter your password: ")
	login_data = '["' + user_name + '", "' + password + '"]'
	HEADER["Content-Length"] = str(len(login_data))

	print("Logging in...")
	resp = requests.post(URL, data=login_data, headers=HEADER)
	res_txt = resp.text
	if 'Login Failure' in res_txt:
		exit("Password does not match")
	else:
		print("Logged in!")

	USER_DATA = (res_txt.split(',')[4].split(':')[1], res_txt.split('}')[1].replace(',', '').replace(':', '=').replace('"',''), user_name)


def login_data():
	return USER_DATA