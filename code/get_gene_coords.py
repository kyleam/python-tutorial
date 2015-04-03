"""Get coordinates from gencode file

usage: python get_gene_coords.py GENES OUTFILE

Arguments:
  GENES      a list of newline-delimited genes
  OUTFILE
"""
import sys

if len(sys.argv) != 3:
    sys.exit(__doc__)

gene_file = sys.argv[1]

with open(gene_file) as infh:
    filecontent = infh.read()

filecontent = filecontent.strip()  # remove trailing new line
genes = filecontent.split('\n')

## now we have genes of interest in list `genes`
## need to read in gtf file, find lines with matching genes,
## and extract coordinates

gencode_file = '../data/gencode-v10-50random.gtf'
outfile = sys.argv[2]
outfh = open(outfile, 'w')

with open(gencode_file) as genfh:
    for line in genfh:
        fields = line.split('\t')  ## newline -> \n
        chrm = fields[0]  ## REV
        start = fields[3]
        stop = fields[4]
        geneinfo = fields[8]

        for desired_gene in genes:  ## REV: inefficient
            ## Add quotes around desired gene name to ensure unique
            ## match
            genematch = '"' + desired_gene + '"'  ## REV
            if genematch in geneinfo:
                outfh.write(','.join([desired_gene, chrm, start, stop]) + '\n')
                break  ## "continue" goes to next iteration
outfh.close()
