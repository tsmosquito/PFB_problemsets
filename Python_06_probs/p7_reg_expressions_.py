#!/usr/bin/env python3

#Problem 1

# import re

# nobodies_found_pos = []

# line_count = 0

# with open("nobody.txt", 'r') as nobody_fh : 
#     # contents = nobody_fh.read() #code for testing if your file actually has contents
#     # print(contents)
#     for line in nobody_fh :
#         nobodies_found_pos = re.finditer(r"Nobody", line)
#         line_count += 1
#         for pos in nobodies_found_pos :
#             print(f"In line {line_count}, the word 'Nobody' starts at position {pos.start()+1}")

#Problem 2 With exceptions added from problem set 9

import re
import sys
subs = ''

try:
    with open(sys.argv[1], 'r') as nobody_fh, open("nobody_name_sub.txt","w") as nobody_write_fh : 
        first_char = nobody_fh.read(1)   ###Note that this almost works as expected: it just    
        if not first_char :              ###removes the first character from the file and so kinda messes with its function
            raise ValueError
        for line in nobody_fh :
            next_line = re.sub(r"Nobody", "Walter", line)
            subs += next_line
        #print(subs) #test to see if it works
        nobody_write_fh.write(f"{subs}\n")
except ValueError:
        print("File is empty")
except IOError:
    print("Looks like the file you supplied might not be in the same folder, might not exist, or that the name might be misspelled")
except IndexError:
    print("""Looks like you forgot to provide a file in the same command prompt line when you ran this program. 
    Run it with the following syntax: ./program_name name_of_file_in_same_directory.txt""")
#Problem 3/4

# import sys
# import re

# with open(sys.argv[1], 'r') as fasta_fh : 
#     for line in fasta_fh :
#         line.rstrip()
#         search_res = re.search(r'^>(\S+)(.*)', line) 
#         if search_res :
#             print(f"id: {search_res.group(1)} desc: {search_res.group(2)}")
       
        # if search_res == None : ###FAILED METHOD!!!!
        #     pass
        # else: 
        #     sub_search_res = re.search(r"(>)(\s+)", line)
        #     print(search_res.group())
        #     print(sub_search_res.group())
        #     #print(f"id: {sub_search_res.group(1)} desc: {sub_search_res.group(2)}")

#Problem 5 FASTA parser

# import sys
# import re

# with open(sys.argv[1], 'r') as fasta_fh : 
#     for line in fasta_fh :
#         line.rstrip()
#         search_res = re.search(r'^>(\S+.*)', line)  
#         if search_res :
#             print(f"id: {search_res.group(1)}")
#         else:
#             search_res2 = re.search(r'([ATCG]*)', line)
#             print(search_res2.group(1))
        
#Problem 6

# import sys
# import re

# with open(sys.argv[1], 'r') as fasta_fh : 
#     for line in fasta_fh :
#         line.rstrip()
#         search_res = re.search(r'([GA]AATT[CT])', line)  
#         if search_res :
#             print(f"id: {search_res.group(1)}")

#Problem 7

# import sys
# import re

# search_string =''

# with open(sys.argv[1], 'r') as fasta_fh : 
#     for line in fasta_fh :
#         line.rstrip()
#         search_res = re.search(r'^>(\S+.*)', line)  
#         if search_res :
#             pass
#         else:
#             search_res2 = re.search(r'([ATCG]*)', line)
#             search_string += search_res2.group(1)
#         search_sub = re.sub(r'(([GA])AATT([CT]))', r'\g<2>^AATT\g<3>', search_string)  
#     print(search_sub)

#Problem 8

# import sys
# import re

# search_string =''

# with open(sys.argv[1], 'r') as fasta_fh : 
#     for line in fasta_fh :
#         line.rstrip()
#         search_res = re.search(r'^>(\S+.*)', line)  
#         if search_res :
#             pass
#         else:
#             search_res2 = re.search(r'([ATCG]*)', line)
#             search_string += search_res2.group(1)
#         search_sub = re.sub(r'(([GA])AATT([CT]))', r'\g<2>^AATT\g<3>', search_string)  

# frag_list = search_sub.split('^')
# frag_list_leng_sorted = sorted(frag_list, key=len)
# print(frag_list_leng_sorted)   

# Problem 9

# import sys
# import re

# enz_dict = {}
# line_count = 0

# with open(sys.argv[1], 'r') as enzyme_list_fh : 
#     for line in enzyme_list_fh :
#         line = line.strip() 
#         if line_count < 10 : #This is a sneaky way to get past the first 10 lines
#             line_count +=1
#         else:
#             split_line = re.split(r'\s{2,}', line) # splits lines by 2 or more whitespaces, returns list
#             enz_dict[split_line[0]] = split_line[-1] #adds last and first element of list as key and value of dictionary
#     print(enz_dict)

#problem 10 ###THIS PROBLEM IS INCREDIBLY DIFFICULT AND I STOPPED MID WAY

#1) import name of enzyme and import/parse fasta 2) load our dictionary 3)compare to dictionary 4)print out sequence with annoatated cut sites, the gragment in their 

# import sys
# import re

# ###Gets the dictionary
# enz_dict = {}
# line_count = 0

# with open(sys.argv[1], 'r') as enzyme_list_fh : 
#     for line in enzyme_list_fh :
#         line = line.strip() 
#         if line_count < 10 : #This is a sneaky way to get past the first 10 lines
#             line_count +=1
#         else:
#             split_line = re.split(r'\s{2,}', line) # splits lines by 2 or more whitespaces, returns list
#             enz_dict[split_line[0]] = split_line[-1] #adds last and first element of list as key and value of dictionary
#     #print(enz_dict) #This works so you can comment it out unless you want to see it again

# ###search dictionary, return value of enzyme name

# key = sys.argv[2]
# key_true_false = key in enz_dict
# if key_true_false == False :
#     print("Error: this key is not in the dictionary")
# else: 
#     cut_site = enz_dict[sys.argv[2]]
#     #print(search_pattern) #this works, tested

# ###Now need need modify the cut site to make it standard




