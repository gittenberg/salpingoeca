"""
Script to call blat on a large number of mRNA transcripts (queries) against one DNA database
"""

from Bio import SeqIO
from subprocess import call

transcripts = "/home/martin/Research/salpingoeca/salpingoeca_rosetta_1_transcripts.fasta"
database = "/home/martin/Research/salpingoeca/salpingoeca_rosetta_1_supercontig_1.3.fasta"

records = list(SeqIO.parse(transcripts, "fasta"))
dna = list(SeqIO.parse(database, "fasta"))[0].seq

for i, transcript in enumerate(records[:10]):
    print i, transcript.seq
    with open("example.fasta", "w") as output_handle:
        SeqIO.write(transcript, output_handle, "fasta")
    #call("/home/martin/blat/blat {0} example.fasta {1}.psl".format(database, str(i)))
    call("/home/martin/blat/blat /home/martin/Research/salpingoeca/salpingoeca_rosetta_1_supercontig_1.3.fasta example.fasta output.psl")
