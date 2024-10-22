#!/usr/bin/env python3

# dnyay = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT'''

# import re

# def nt_60_chars_func(dna):
#     dna_no_new_lines = dna.rstrip()
#     lines_with_new_lines = (re.sub("(.{60})", "\\1\n", dna_no_new_lines))
#     return lines_with_new_lines

# # print(nt_60_chars_func(dnyay))

# #Problem 2

# import re

# def nt_60_chars_func(dna):
#     dna_no_new_lines = dna.replace("\n", "")
#     lines_with_new_lines = (re.sub("(.{60})", "\\1\n", dna_no_new_lines))
#     return lines_with_new_lines

# print(nt_60_chars_func(dnyay))

# #Problem 3 #NB THIS FUNCTION DOES NOT WORK not sure why I thought it did or was able to get working output before (maybe was runnign something else in parallel)

# import re

# def nt_60_chars_func(dna, line_length):
#     dna_no_new_lines = dna.replace("\n", "")
#     lines_with_new_lines = (re.sub("(.{line_length})", "\\1\n", dna_no_new_lines))
#     return lines_with_new_lines

# print(nt_60_chars_func(dnyay, 10))

#Problem 4 #Solved! Function works great!

# import re
# import sys

# def fasta_parser(fasta_fh):
#     fasta_dict = {}
#     gene_header = '' #you can technically just define this in the if (if it's in both teh if and else) loop because python assumes you want to expand its scope
#     for line in fasta_fh :
#         line = line.strip()
#         search_res = re.search(r'^(>\S+).*', line)
#         if search_res:
#             gene_header = search_res.group(1)
#             fasta_dict[gene_header] = '' ##can also call the string function as empty str()
#         else:
#             fasta_dict[gene_header] += line
#     return fasta_dict

# def fasta_line_length_changer(fasta_dict, line_length):
#     for key in fasta_dict:
#         seq_to_sub = fasta_dict[key] #take a given key's value as string
#         fasta_dict[key] = (re.sub(f"(.{{{line_length}}})", r"\1\n", seq_to_sub))
#     return fasta_dict #ultimately want to make a new dictioanry or append values if possible?

# with open(sys.argv[1]) as fasta_fh, open('fasta_new_line_length.txt', 'w') as fasta_new_line_length_fh:
#     modified_fasta = fasta_line_length_changer(fasta_parser(fasta_fh), sys.argv[2])
#     for key in modified_fasta:
#         fasta_new_line_length_fh.write(f"{key}\n{modified_fasta[key]}\n") #adding a new line character at the end so that each new header sequence

#Problem 5  #SOLVED this works fine

# dnyay = 'GGGGGGGGGCCCTA'

# def gc_counter(dna):
#     g_count = dna.count('G')
#     c_count = dna.count('C')
#     gc_content = (g_count + c_count)/len(dna)
#     return round(gc_content, 2)

# test_result = gc_counter(dnyay)

# print(test_result)

#Problem 6 SOLVED this works

# dnyay = 'GGGGGGGGGCCCTA'

# def rev_complimenter(dna_seq):
#     compliment = dna_seq.replace('G','c').replace('C','g').replace('T','a').replace('A','t') #gets compliment
#     rev_compliment = compliment[::-1] #reverses the string
#     return rev_compliment.upper()

# print(rev_complimenter(dnyay))

#Problem 7

import subprocess
subprocess.run('ls -l', shell=True)
