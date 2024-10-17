#!/usr/bin/env python3

import sys

#puts your input into variable string_to_search
string_to_search = sys.argv[1] 

new_string = string_to_search.replace('GAATTC', "G^AATTC") 

string_list = new_string.split('^') #splits string on ^


for string in string_list : #gives start position, end position, and length
    frag_length = len(string)
    string_index_start = string_to_search.index(string)
    string_index_end = string_index_start + frag_length
    print(f"The fragment length is: {frag_length}, "
        f"it starts at: {string_index_start + 1}, " #note off by one error gets corrected here
        f"and ends at: {string_index_end +1}") 

