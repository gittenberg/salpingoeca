infile = '/home/martin/Research/salpingoeca/sra_data.fastq'

fastq_1 = open('/home/martin/Research/salpingoeca/fastq_r1.fastq', 'w+')
fastq_2 = open('/home/martin/Research/salpingoeca/fastq_r2.fastq', 'w+')

import time
print time.strftime('%X %x %Z')

for i, line in enumerate(open(infile)):
    # print progress every 10000 lines
    if not i % 10000:
        print i
    fastq_1.write(line) if (i % 8 < 4) else fastq_2.write(line)

fastq_1.close()
fastq_2.close()
