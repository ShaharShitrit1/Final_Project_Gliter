import requests
import headers
import login
import datetime

def change_post_data(url):
    LOGIN_DATA = login.login_data()
    header = headers.get_headers()
    header["Cookie"] = LOGIN_DATA[1]
    resp = requests.get(url, headers=header)
    print(resp)


def text_color():
    LOGIN_DATA = login.login_data()
    USER_NAME = LOGIN_DATA[0]
    x = input("enter text color: ")
    url = f'http://cyber.glitter.org.il/glit?id=-1&feed_owner_id={USER_NAME}&publisher_id={USER_NAME}&publisher_screen_name=shahar&publisher_avatar=im3&background_color=white&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&content=fontChange&font_color={x}'
    change_post_data(url)


def background_color():
    LOGIN_DATA = login.login_data()
    USER_NAME = LOGIN_DATA[0]
    x = input("enter background color: ")
    url = f'http://cyber.glitter.org.il/glit?id=-1&feed_owner_id={USER_NAME}&publisher_id={USER_NAME}&publisher_screen_name=shahar&publisher_avatar=im3&background_color={x}&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&content=backgroundChange&font_color=black'
    change_post_data(url)


def change_date():
    LOGIN_DATA = login.login_data()
    USER_NAME = LOGIN_DATA[0]
    url = f'http://cyber.glitter.org.il/glit?id=-1&feed_owner_id={USER_NAME}&publisher_id={USER_NAME}&publisher_screen_name=shahar&publisher_avatar=im3&background_color=white&date=2055-06-09T16:19:33.224Z&content=dateChange&font_color=black'
    change_post_data(url)


def change_avatar():
    LOGIN_DATA = login.login_data()
    USER_NAME = LOGIN_DATA[0]
    x = 'one'

    while True:
        try:
            int(x)
            break;
        except ValueError:
            while x < '0' or x > '8':
                x = input("enter new avatar num(1-8): ")

    url = f'http://cyber.glitter.org.il/glit?id=-1&feed_owner_id=8810&publisher_id=8810&publisher_screen_name=shahar&publisher_avatar=im{x}&background_color=white&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&content=avatarChange&font_color=black'
    change_post_data(url)


def bold_post():
    LOGIN_DATA = login.login_data()
    USER_NAME = LOGIN_DATA[0]
    bold_word = "%3Ch1%3E" + 'yaronMyMen' + '%3C'

    url = f'http://cyber.glitter.org.il/glit?id=-1&feed_owner_id={USER_NAME}&publisher_id={USER_NAME}&publisher_screen_name=shahar&publisher_avatar=im3&background_color=white&date={datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z&content={bold_word}&font_color=black'
    change_post_data(url)