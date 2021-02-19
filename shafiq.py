import random

import string

import itertools

import threading

import time

import sys

 

done = False

#here is the animation

def animate():

    for c in itertools.cycle(['|', '/', '-', '\\']):

        if done:

            break

        sys.stdout.write('\rloading ' + c)

        sys.stdout.flush()

        time.sleep(0.1)

    sys.stdout.write('\rReady!     ')

 

t = threading.Thread(target=animate)

 

print(""" 

╭━━━┳╮╱╭┳━━━┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭━╮┃╭━━┫╭━╮┃
┃╰━━┫╰━╯┃┃╱┃┃╰━━┫┃╱┃┃
╰━━╮┃╭━╮┃╰━╯┃╭━━┫┃╱┃┃
┃╰━╯┃┃╱┃┃╭━╮┃┃╱╱┃╰━╯┃
╰━━━┻╯╱╰┻╯╱╰┻╯╱╱╰━━━╯

                                            

""")                                                                                  

A = """

<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

<      snapchat.com/add/br35308        >

<      instagram/sha_fo_ka        >

<      PROGRAMING/SHAFO           >

<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

 

"""

print ("")

print(A)

t.start()

time.sleep(1)

done = True

 

t = 0

userT = input(' : ')

lengthPrint = int(input('How many times: '))

file = open('usernames.txt', 'w')

 

while t != lengthPrint:

  x=userT

  file.write(str(x) +'\r\n')

  t = t + 1

 

file.close()
