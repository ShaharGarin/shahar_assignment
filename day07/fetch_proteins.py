from Bio import Entrez
import sys
from datetime import datetime as dt

Entrez.email = "shahar.garin@gmail.com"
file_limit = 10000



def main():
    search = search_protein()
    files_download(search)
    log_maker(search)



def search_protein():
    if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
        exit("Please provide search term and numberof files to download")
    if float(sys.argv[2]) > file_limit:
        exit("Too many files. NCBI limits download to 10,000")
    handle = Entrez.esearch(db = "protein", retmode = "txt", term = sys.argv[1], idtype = "acc", retmax = sys.argv[2])
    protein_search = Entrez.read(handle)
    handle.close()
    return protein_search


def files_download(search_dic):
    for ide in search_dic["IdList"]:
        fetch = Entrez.efetch(db = "protein", id = ide, rettype = "fasta", retmode = "fasta")
        file = f"{sys.argv[1]}_sequence_{ide}.fna"
        with open(file, 'w') as pf:
            pf.write(fetch.read())
        print(file)
        fetch.close()
    return

def log_maker(search_dic):
    log_name = "protein_search_log.csv"
    with open(log_name, 'a') as log:
        log.write(f"{dt.now().strftime("%m/%d/%Y %H:%M:%S"), sys.argv[1], sys.argv[2], search_dic["Count"]}\n")
    return
    

main()
