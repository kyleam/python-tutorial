"""
To merge files with one common column (should it be first columns?)
USAGE: to merge two files with a common column. Common column should be the first column

"""
import sys

datesfile = sys.argv[1]
#datesfile = '../data/programs_dates.csv'

prog_dates = {}
with open(datesfile) as datefh:
    for line in datefh:
        program, date = line.strip().split(',')
        #print(program)
        prog_dates[program]  = date
#print(prog_dates['Firefox'])

outfile = 'task3.txt'
outfh = open(outfile,'w')
verfile = '../data/program-versions.csv'
with open(verfile) as verfh:
    for line in verfh:
        program, version = line.strip().split(',')
        outfields = [program, prog_dates[program], version]
        outfh.write(','.join(outfields) + '\n')
outfh.close()
