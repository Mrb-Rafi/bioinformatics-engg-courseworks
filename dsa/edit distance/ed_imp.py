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
#     out_handle = open(filename, "w")
#     out_handle.write(net_handle.read())
#     out_handle.close()
#     net_handle.close()
#     print("Saved")

# print("Parsing...")
# record = SeqIO.read(filename, "fasta")
# print(record)

temp = net_handle.read()

gene = ""

for i in temp:
    if 