#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num= abs(number)%10

message= "Last digit of {} is {} ".format(number,last_num)

if last_num>5:
	message += "and is greater than 5"
elif last_num==0:
	message += "and is 0"
else: 
	last_num<6 and number !=0
	message += "and is less than 6 and not 0"
	
print(message)

