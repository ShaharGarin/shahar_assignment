import os
import Bio
import Bio.SeqIO
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filepath', help = 'fasta file path')
parser.add_argument('--duplicate', required = False, action = 'store_true', help = 'Find largest duplicate sequence in file')
parser.add_argument('--start', required = False, action = 'store_true', help = 'Find gene start codon')
user_arg = parser.parse_args()

def main():
    check_args()
    if user_arg.duplicate:
        dup = find_dup()
        print (f"The longest repeating sequence is {dup}")
    if user_arg.start:
       print(find_start())

def check_args():
    if not user_arg.duplicate and not user_arg.start:
        parser.error("No mode(s) of action selected. Run with --duplicate or --start")
    if not os.path.isfile(user_arg.filepath):
        exit("Path given is incorrect. Try Again.")


def find_dup():
    file = Bio.SeqIO.read(user_arg.filepath, 'fasta')
    seq = str(file.seq)
    length = 1
    result = ''
    while True:
        dna_regex = r'([ATGC]{' + str(length) + r'}).*\1'
        match = re.search(dna_regex, str(seq), flags = re.IGNORECASE)
        if match:
            result = match.group(1)
            length += 1
        else:
            break
    return result

def find_start():
    file = Bio.SeqIO.read(user_arg.filepath, 'fasta')
    seq = str(file.seq)
    start_codon = re.search('atg', seq, flags = re.IGNORECASE)
    
    if not start_codon:
        return "No start codon identified."
    else:
        location = start_codon.start()
        return f"The start codon begins at index {location}."
    
main()