#!/usr/bin/env python3

taxa_string = 'sapiens : erectus : neanderthalensis'

taxa_list = taxa_string.split(':')

print(f" {sorted(taxa_list, key = len)}")
