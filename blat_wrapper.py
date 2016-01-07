"""
Script to call blat on a large number of mRNA transcripts (queries) against one DNA database
"""

import os
from Bio import SeqIO
from subprocess import call

def file_len(fname):
    """
    Auxiliary function to return number of lines in file fname
    :param fname: file name
    :return: number of lines
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

transcripts = "/home/martin/Research/salpingoeca/salpingoeca_rosetta_1_transcripts.fasta"
database = "/home/martin/Research/salpingoeca/salpingoeca_rosetta_1_supercontig_1.3.fasta"

records = list(SeqIO.parse(transcripts, "fasta"))
#dna = list(SeqIO.parse(database, "fasta"))[0].seq

for i, transcript in enumerate(records[10:30]):
    print i, transcript.seq
    with open("example.fasta", "w") as output_handle:
        SeqIO.write(transcript, output_handle, "fasta")
    current_outputfile = str(i).zfill(5) + ".psl"
    call("/home/martin/blat/blat {0} example.fasta {1}".format(database, current_outputfile), shell=True)

    # only keep file if matches were found:
    if file_len(current_outputfile) <= 6:
        os.remove(current_outputfile)
