#!/usr/bin/env python3

import sys

string_to_count = sys.argv[1] #puts your input into variable string_to_count

string_to_count.upper() #makes everything the same case

as_in_string = string_to_count.count('A') #counts for each letter
cs_in_string = string_to_count.count('C')
ts_in_string = string_to_count.count('T')
gs_in_string = string_to_count.count('G')

print(f"A:{as_in_string}, C:{cs_in_string}, T:{ts_in_string}, G:{gs_in_string}")
