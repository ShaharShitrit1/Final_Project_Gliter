import post_msg
import like
import load_glits
from cookie_challenge import get_user_cookie, get_user
from login import login

LOGIN_DATA = login()
MENU = '''0 <-> exit
1 <-> get like
2 <-> change font color (post)
3 <-> change background color (post)
4 <-> change date (post)
5 <-> change avatar (post)
6 <-> upload bold post
7 <-> load more than 2 glits at one time
8 <-> load posts from someone else's feed
9 <-> cookie challenge'''


def print_menu_and_funcs():
	print(MENU)

	x = 'NULL'

	while True:
		try:
			int(x)
			break;
		except ValueError:
			x = input("Enter your chooice: ")

	if int(x) == 0:
		exit(1)

	call_functions(int(x))
	print("\n")


def call_functions(x):
	if(x == 1):
		like.moreLikes()

	elif (x == 2):
		post_msg.text_color()

	elif (x == 3):
		post_msg.background_color()

	elif (x == 4):
		post_msg.change_date()

	elif (x == 5):
		post_msg.change_avatar()

	elif (x == 6):
		post_msg.bold_post()

	elif (x == 7):
		load_glits.more_glits_one_load()

	elif (x == 8):
		load_glits.load_another_feed()

	elif (x == 9):
		print(get_user_cookie(get_user()))

	else:
		print("Make sure you choose num between 0 - 10")



def main():

	while(True):
		print_menu_and_funcs()

if __name__ == '__main__':
	main()