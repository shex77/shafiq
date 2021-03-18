try:  

    import requests 

    import uuid 

    import time 

except Exception as e: 

    print(e) 

logo = ("""

  FOLLOW ME IN INSTAGRAM

       < @rab1it >

    FOR ANY ERRORS TELL ME IN TELEGRAM

       < erh4b > 

•••••••••

""")

 

print(logo) 

user = input('usernamet bnusa: ') 

password = input('passwordy instat bnusa: ') 

target = str(input(("away reporty le aday:"))) 

sle = int(input("chan sanya: "))

def login(): 

    global target 

    r = requests.Session() 

 

    uid = str(uuid.uuid4()) 

 

    url = "https://i.instagram.com/api/v1/accounts/login/" 

 

    headers = { 

        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 

        "Accept": "*/*", 

        "Accept-Encoding": "gzip, deflate", 

        "Accept-Language": "en-US", 

        "X-IG-Capabilities": "3brTvw==", 

        "X-IG-Connection-Type": "WIFI", 

        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 

        'Host': 'i.instagram.com' 

    } 

 

    data = { 

        '_uuid': uid, 

        'username': user, 

        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password), 

        'queryParams': '{}', 

        'optIntoOneTap': 'false', 

        'device_id': uid, 

        'from_reg': 'false', 

        '_csrftoken': 'missing', 

        'login_attempt_count': '0' 

    } 

 

    loginreq = r.post(url, data=data, headers=headers, allow_redirects=True) 

    print(loginreq.text) 

 

 

    if loginreq.text.find("is_private") >= 0: 

        done = 0 

        print("daxl buy") 

        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']}) 

        url_id = "https://www.instagram.com/{}/?__a=1".format(target) 

        url_get_user_id = r.get(url_id).json() 

        print(url_get_user_id) 

        while True: 

            user_id = str(url_get_user_id["logging_page_id"]) 

            your_user_id = str(user_id.split("_")[1])# 4231341234

            urlRep = "https://i.instagram.com/users/" + your_user_id + "/report/" 

            datas = {  

                    'source_name': '', 'reason_id': 2, 'frx_context': ''  # self injury

                } 

            req_SessionID = r.post(urlRep, data=datas) 

            done += 1 

            print(f"self kra  : : {done}") 

            time.sleep(0.1) 

    else: 

        print("daxl nabuy tkaya dubaray kawa!") 

login()
