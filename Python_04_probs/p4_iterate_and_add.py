#!/usr/bin/env python3

iterate_list = [101,2,15,22,95,33,2,27,72,15,52]
iterate_list.sort()

new_list_even = []
new_list_odd = []

for num in iterate_list:
	if num% 2 == 0:
		new_list_even.append(num)
		print(num)
	elif num% 2 != 0:
		new_list_odd.append(num)
		print(num)
	else:
		print("Ahh, something's wrong!!!")
sum_even = sum(new_list_even)
sum_odd = sum(new_list_odd)

print(f"""This is the sorted list: {iterate_list}.
The sum of the even numbers is {sum_even}
The sum of the odd number is {sum_odd}""")
