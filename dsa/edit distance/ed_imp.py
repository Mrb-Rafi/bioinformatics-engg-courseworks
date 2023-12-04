import os
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
filename = "gene.txt"
if not os.path.isfile(filename):
    # Downloading...
    net_handle = Entrez.efetch(
        db="nucleotide", id="1124779319", rettype="fasta", retmode="text"
    )

temp = net_handle.read()

gene = ""

for i in temp:
    if 