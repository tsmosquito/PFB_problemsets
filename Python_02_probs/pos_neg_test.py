#!/usr/bin/env python3

import sys
fly = int(sys.argv[1])

print("the number", fly, "is being tested")

if fly < 0:
        print("not buzzing cause negative numbah")
elif fly > 0:
	if fly < 50:
		print("buzz with a beat cause less than fifty")
		if fly % 2 == 0:
			print("buzz with equal wingbeat amplitude cause even")
	elif fly > 50:
		print("more than 50 buzz")
		if fly % 3 == 0:
			print("your number buzzes with a hox gene because it's divisable by 3")
		else:
        		print ("a buzz not divisible by 3")
	elif fly == 50:
		print("fly is 50 exactly")
else:
	print("fly is equl to zero, sad fly")
