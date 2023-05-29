import requests
import headers
import login

URL = "http://cyber.glitter.org.il/likes/"

def moreLikes():
    glit_id = input("Enter the glit id that will get likes: ")
    LOGIN_DATA = login.login_data()
    POST_DATA = '{"glit_id":' + glit_id + ',"user_id":' + LOGIN_DATA[0] + ',"user_screen_name":"' + LOGIN_DATA[2] + '","id":-1}'
    header = headers.get_headers()
    header["Cookie"] = LOGIN_DATA[1].replace('"', '')
    resp = requests.post(URL, data=POST_DATA, headers=header)

    if "Server Failure" in resp.text:
    	print("make sure you entered a valid glit id")
    else:
    	print("the program did what you asked for")