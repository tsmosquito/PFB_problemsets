#!/usr/bin/env python3

import sys

string_to_replace = sys.argv[1] #puts your input into variable string_to_count

string_Ts_to_Us = string_to_replace.upper().replace('T','U') #replace Ts to Us

print(f"Your new sequence is with Ts turned to Us is: {string_Ts_to_Us}")
