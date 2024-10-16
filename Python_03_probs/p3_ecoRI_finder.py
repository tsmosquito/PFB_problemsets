#!/usr/bin/env python3

import sys

string_to_search = sys.argv[1] #puts your input into variable string_to_search

start_index = string_to_search.upper().find('GAATTC')

end_index = int(string_to_search.upper().find('GAATTC')) + 6

print(f"EcoRI start and end are {start_index}:{end_index}")


