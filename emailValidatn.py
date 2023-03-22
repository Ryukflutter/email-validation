
#Email Validation 

import re
from faker import Faker
import time



mail_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

for i in range(10):
#	user_email = input("Enter your email --> ")
	for i in range(5):
		fake = Faker()
		if re.search(mail_pattern, fake.free_email()):
			print(fake.free_email())
			time.sleep(1)
			print("your email is right!\n")
			break
		else:
			print("wrong mail, type correct mail!")
			continue


#Don't Recommended method2 use method1 

#-------------<Method2>----------

'''
usermail = input("enter email: ")#w@w.in
d,j,k=0,0,0
if usermail[0].isalpha():
	if len(usermail)>=6:
		if (usermail[-4]==".") ^ (usermail[-3]=="."):
			if ("@" in usermail) and (usermail.count("@")==1):
				for i in usermail:
					if i == i.isspace():
						k=1
					elif i.isalpha():
						if i== i.upper():
							j=1
					elif i.isdigit():
						continue
					elif i=="_" or i=="." or i =="@":
						print("great")
						
					else:
						d= 1
				if k==1 or j== 1 or d==1:
					print("wrong email please check ")
			else:
				print("Wrong email [@]..!")
		else:
			print("Enter right email..! (.)")
	else:
		print("Enter right email..![length of email > 6]")
else:
	print("Enter right email..!\noh..! you eventually used digits in your mail it should be alpha...")
'''