#!/usr/bin/env python3

import sys

string_to_count = sys.argv[1] #puts your input into variable string_to_count

total_count = len(string_to_count) #takes length

as_in_string = string_to_count.upper().count('A') #counts for each letter
ts_in_string = string_to_count.upper().count('T')

at_prop = (int(as_in_string) + int(ts_in_string))/int(total_count) #add everything and divide, make integers first

print(f"AT proportion is {at_prop:.2%}")
