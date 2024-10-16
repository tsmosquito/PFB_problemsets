#!/usr/bin/env python3

import sys

string_to_count = sys.argv[1] #puts your input into variable string_to_count

dna_compliment = string_to_count.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')

reverse_compliment = dna_compliment[::-1]

print(f"The reverse compliment is {reverse_compliment.upper()}")


