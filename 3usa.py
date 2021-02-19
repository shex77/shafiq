import os
import random


os.system("clear")

lost = """


 $$$$$$\                                
$$ ___$$\                               
\_/   $$ |$$\   $$\  $$$$$$$\  $$$$$$\  
  $$$$$ / $$ |  $$ |$$  _____| \____$$\ 
  \___$$\ $$ |  $$ |\$$$$$$\   $$$$$$$ |
$$\   $$ |$$ |  $$ | \____$$\ $$  __$$ |
\$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$ |
 \______/  \______/ \_______/  \_______|
                                        
                                        
                                        
   
                                  
"""


def asia():
	op = open("asia.txt","w")
	os.system("clear")
	print(lost)
	e = "133"
	for x in range(9999999999):
		c = "1234567890"
		x1 = random.choice(c)
		x2 = random.choice(c)
		x3 = random.choice(c)
		x4 = random.choice(c)
		x5 = random.choice(c)
		x6 = random.choice(c)
		x7 = random.choice(c)
		x8 = random.choice(c)
		x9 = random.choice(c)
		x10 = random.choice(c)
		x11 = random.choice(c)
		x12 = random.choice(c)
		x13 = random.choice(c)
		x14 = random.choice(c)
		b = "*"+e+"*"+x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+"#"
		print(b)
		op.write(b+"\n")

def kor():
	op = open("korak.txt","w")
	os.systm("clear")
	print(lost)
	e = "221"
	for x in range(99999):
		c = "1234567890"
		x1 = random.choice(c)
		x2 = random.choice(c)
		x3 = random.choice(c)
		x4 = random.choice(c)
		x5 = random.choice(c)
		x6 = random.choice(c)
		x7 = random.choice(c)
		x8 = random.choice(c)
		x9 = random.choice(c)
		x10 = random.choice(c)
		x11 = random.choice(c)
		x12 = random.choice(c)
		x13 = random.choice(c)
		x14 = random.choice(c)
		b = "*"+e+"*"+x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+"#"
		print(b)
		op.write(b+"\n")
	

def dr():
		print(lost)
		print("=======================")
		print(" Drus Krdny Carty Asia wKorek")
		print("99 Hazar kart testykan")
		print("[1] Asia")
		print("[2] Korek")
		print("=======================")
		z = int(input("Yakekyan Halbzhera : "))
		if z==1:
			os.system("clear")
			asia()
		elif z==2:
			os.system("clear")
			kor()
			
dr()
		
	


	

	