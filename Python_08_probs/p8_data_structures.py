#!/usr/bin/env python3

import re
import sys

fasta_dict = {}
gene_header = ''

with open("Python_08.fasta", 'r') as fasta_fh : 
    for line in fasta_fh :
        line = line.rstrip()
        search_res = re.search(r'^>(\S+).*', line)  
        if search_res is not None :
            gene_header = search_res.group(1)
            fasta_dict[search_res.group(1)] = ''
        else:
            fasta_dict[gene_header] += line
    #print(fasta_dict) #this works!


nt_comp = {'A':0,'G':0,'T':0,'C':0}

for gene in fasta_dict :
    seq = fasta_dict[gene]
    
    nt_comp = {'A':0,'G':0,'T':0,'C':0}
    
    nt_comp['A'] = seq.count('A')
    nt_comp['C'] = seq.count('C')
    nt_comp['G'] = seq.count('G')
    nt_comp['T'] = seq.count('T')
    
    fasta_dict[gene] = [seq, nt_comp]

#print(fasta_dict['c0_g1_i1'][1]['A'])

# for gene in fasta_dict:
#     print(f"seqs[{gene}] ['A'] = {fasta_dict[gene][1]['A']}")
#     print(f"seqs[{gene}] ['T'] = {fasta_dict[gene][1]['T']}")
#     print(f"seqs[{gene}] ['C'] = {fasta_dict[gene][1]['C']}")
#     print(f"seqs[{gene}] ['G'] = {fasta_dict[gene][1]['G']}\n\n")

#Problem 2

# codons = []

# for gene in fasta_dict:
#     seq = fasta_dict[gene][0]
#     codons = [(seq[i:i+3]) for i in range(0, len(seq), 3)]

#     nt_comp = {'A':0,'G':0,'T':0,'C':0}
    
#     nt_comp['A'] = seq.count('A')
#     nt_comp['C'] = seq.count('C')
#     nt_comp['G'] = seq.count('G')
#     nt_comp['T'] = seq.count('T')

#     fasta_dict[gene] = [seq, nt_comp, codons]
    
#     print(f"seq: {gene} \nframe 1 codons: {fasta_dict[gene][2]}\n\n")

    ### problem 3

# frame_1 = []
# frame_2 = []
# frame_3 = []

# for gene in fasta_dict:
#     seq = fasta_dict[gene][0]
#     frame_1 = [(seq[i:i+3]) for i in range(0, len(seq), 3)]
#     frame_2 = [(seq[i:i+3]) for i in range(1, len(seq), 3)]
#     frame_3 = [(seq[i:i+3]) for i in range(2, len(seq), 3)]
   
#     nt_comp = {'A':0,'G':0,'T':0,'C':0}
    
#     nt_comp['A'] = seq.count('A')
#     nt_comp['C'] = seq.count('C')
#     nt_comp['G'] = seq.count('G')
#     nt_comp['T'] = seq.count('T')

#     fasta_dict[gene] = [seq, nt_comp, frame_1, frame_2, frame_3]
    
#     print(f"seq: {gene} \nframe 1 codons: {fasta_dict[gene][2]}\nand 2 codons: {fasta_dict[gene][3]}\nand 3 codons: {fasta_dict[gene][4]}\n\n")

    ###problem 4

# frame_1 = []
# frame_2 = []
# frame_3 = []
# frame_4 = []
# frame_5 = []
# frame_6 = []

# for gene in fasta_dict:
#     seq = fasta_dict[gene][0]
#     frame_1 = [(seq[i:i+3]) for i in range(0, len(seq), 3)]
#     frame_2 = [(seq[i:i+3]) for i in range(1, len(seq), 3)]
#     frame_3 = [(seq[i:i+3]) for i in range(2, len(seq), 3)]
    
#     dna_compliment = seq.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#     reverse_compliment = dna_compliment[::-1]

#     frame_4 = [(reverse_compliment[i:i+3]) for i in range(0, len(reverse_compliment), 3)]
#     frame_5 = [(reverse_compliment[i:i+3]) for i in range(1, len(reverse_compliment), 3)]
#     frame_6 = [(reverse_compliment[i:i+3]) for i in range(2, len(reverse_compliment), 3)]

#     nt_comp = {'A':0,'G':0,'T':0,'C':0}
    
#     nt_comp['A'] = seq.count('A')
#     nt_comp['C'] = seq.count('C')
#     nt_comp['G'] = seq.count('G')
#     nt_comp['T'] = seq.count('T')

#     fasta_dict[gene] = [seq, nt_comp, frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
    
#     print(f"seq: {gene} \nframe 1 codons: {fasta_dict[gene][2]}\nand 2 codons: {fasta_dict[gene][3]}\nand 3 codons: {fasta_dict[gene][4]}\nand 4 codons: {fasta_dict[gene][5]}\nand 5 codons: {fasta_dict[gene][6]}\nand 6 codons: {fasta_dict[gene][7]}\n\n")

#problem 5

import re

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

frame_1 = []
frame_2 = []
frame_3 = []
frame_4 = []
frame_5 = []
frame_6 = []

for gene in fasta_dict:
    seq = fasta_dict[gene][0]
    frame_1 = [(seq[i:i+3]) for i in range(0, len(seq), 3)]
    frame_2 = [(seq[i:i+3]) for i in range(1, len(seq), 3)]
    frame_3 = [(seq[i:i+3]) for i in range(2, len(seq), 3)]
    
    dna_compliment = seq.upper().replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    reverse_compliment = dna_compliment[::-1]

    frame_4 = [(reverse_compliment[i:i+3]) for i in range(0, len(reverse_compliment), 3)]
    frame_5 = [(reverse_compliment[i:i+3]) for i in range(1, len(reverse_compliment), 3)]
    frame_6 = [(reverse_compliment[i:i+3]) for i in range(2, len(reverse_compliment), 3)]

    nt_comp = {'A':0,'G':0,'T':0,'C':0}
    
    nt_comp['A'] = seq.count('A')
    nt_comp['C'] = seq.count('C')
    nt_comp['G'] = seq.count('G')
    nt_comp['T'] = seq.count('T')

    fasta_dict[gene] = [seq, nt_comp, frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
    
    for codon in frame_1:

with open('Python_08.codons-6frames.nt', 'w') as nt_frames_fh:
    print(f"""seq: {gene} \nframe 1 codons: {fasta_dict[gene][2]}\n
    and 2 codons: {fasta_dict[gene][3]}\n
    and 3 codons: {fasta_dict[gene][4]}\n
    and 4 codons: {fasta_dict[gene][5]}\n
    and 5 codons: {fasta_dict[gene][6]}\n
    and 6 codons: {fasta_dict[gene][7]}\n\n""")

 with open('Python_08.translated.aa', 'w') aa_frames_fh:
    print(f"""seq: {gene} \nframe 1 codons: {fasta_dict[gene][2]}\n
    and 2 codons: {fasta_dict[gene][3]}\n
    and 3 codons: {fasta_dict[gene][4]}\n
    and 4 codons: {fasta_dict[gene][5]}\n
    and 5 codons: {fasta_dict[gene][6]}\n
    and 6 codons: {fasta_dict[gene][7]}\n\n""")