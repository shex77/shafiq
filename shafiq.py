#VX_SH4FO

# instagram : vx_sh4fo

# facebook : Shafo Ka

# telegram : sha fo ka

# Agar Brdt Amazha Ba Nawaka Bka —> @SHAFO

import requests

from time import sleep

username = input("Username: ")

password = input("password: ")

s = requests.session()

headerr = {'accept': '*/*', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 'x-csrftoken': 'missing', 'x-requested-with': 'XMLHttpRequest'}

def login():

   url = 'https://www.instagram.com/accounts/login/ajax/'

   data = {

        'username': username,

        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password}

   loginreq = s.post(url, data=data, headers=headerr)

   if ('"authenticated": false') in loginreq.text:

       print("Login Nabw")

   elif ('"authenticated": true') in loginreq.text:

       print("login bw" + ' »»', username)

       for i in range(11):

           idd = ['192411214', '314216', '25025320', '815393548', '232192182', '289112145', '41797510',

                  '13460080', '43109246', '20269764', '5162610']

           for ids in idd:

               headerr["x-csrftoken"] = loginreq.cookies["csrftoken"]

               hama = 'https://www.instagram.com/web/friendships/' + str(ids) + '/follow/'

               reqfolo = s.post(hama, headers=headerr)

           sleep(120)

           for ids in idd:

               headerr["x-csrftoken"] = loginreq.cookies["csrftoken"]

               software = 'https://www.instagram.com/web/friendships/' + str(ids) + '/unfollow/'

               reqfolo1 = s.post(software, headers=headerr)

           print(f"Done ({str(i)}/11)")

   elif ('"message": "checkpoint_required"') in loginreq.text:

       print("Kawta chkp" + ' »»', username)

       exit()

login()

#VX_SH4FO

