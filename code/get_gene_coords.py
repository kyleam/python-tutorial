"""Get coordinates from gencode file

usage: python get_gene_coords.py
"""

gene_file = '../data/genes-5random.txt'  # REV

infh = open(gene_file)  # REV
filecontent = infh.read()
infh.close()  # REV

filecontent = filecontent.strip()  # remove trailing new line

genes = filecontent.split('\n')

## now we have genes of interest in list `genes`
## need to read in gtf file, find matching lines with matching genes,
## and extract coordinates
