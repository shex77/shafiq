import requests

import random

import string

ld = '\033[1;36m'

sa = 'https://pastebin.com/raw/aTfmynYk'

jd = 'https://pastebin.com/raw/kXPNhAq2'

r = requests.get(jd).text

t = requests.get(sa).text

ee = '\033[1;33m'

RUKS1 = '\033[1;32m'

e = '\033[1;32m'

g ='@gmail.com'

h ='@hotmail.com'

y ='@yahoo.com'

print(ld+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

adfr ="""  __  __               _

 

╭━━━┳╮╱╭┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭━━┫╭━╮┃
┃╰━━┫╰━╯┃╰━━┫┃╱┃┃
╰━━╮┃╭━╮┃╭━━┫┃╱┃┃
┃╰━╯┃┃╱┃┃┃╱╱┃╰━╯┃
╰━━━┻╯╱╰┻╯╱╱╰━━━╯

"""

print(e+adfr)

print(ee+r)

print(ld+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

print('\033[1;31mgmail --> 1\n\033[1;33mhotmail --> 2\n\033[1;32myahoo --> 3\n\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

type = int(input(RUKS1+'[!]halbzhera:'))

if type >3:

	print('\033[1;31mخطا !!')if type <4:

	

	length = int(input('chand user:'))

	RUKS = int(input('chnd wsha:'))

file = open('list.txt', 'w')

if type == 1:

    users = string.ascii_lowercase + string.digits

    print('basrkawtue tawaw')

    leng = 1

    while leng < length:

        file.write(''.join(random.choice(users) for i in range(RUKS))+g+'\r\n')

        leng += 1

##############################

if type == 2:

    users = string.ascii_lowercase + string.digits

    print('Tawaw')

    leng = 1

    while leng < length:

        file.write(''.join(random.choice(users) for i in range(RUKS))+h+'\r\n')

        leng += 1

##############################

if type == 3:

    users = string.ascii_lowercase + string.digits

    leng = 1

    print('tawaw')

    while leng < length:

        file.write(''.join(random.choice(users) for i in range(RUKS))+y+'\r\n')

        leng += 1

        

############################
