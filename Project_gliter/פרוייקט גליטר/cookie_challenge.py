import hashlib
from datetime import datetime, date

NOW = datetime.now()
TODAY = date.today()

def get_user_cookie(user_name):
	md5_user_name = hashlib.md5(user_name.encode())

	current_time = NOW.strftime("%H%M")
	current_time.replace('0', '')

	current_date = TODAY.strftime("%d%m%Y")

	cookie = current_date + '.' + md5_user_name.hexdigest() + '.' + current_time + '.' + current_date

	return cookie


def get_user():

	return input("pls enter user name and you will get the cookie: ")
