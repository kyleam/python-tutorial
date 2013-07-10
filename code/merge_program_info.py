"""Merge program info by program name

usage: merge_program_info.py

REV: how could this script be generalized?
"""

dates_file = '../data/program-dates.csv'
version_file = '../data/program-versions.csv'

prog_dates = {}  # dictionary of dates keyed by program name

with open(dates_file) as datefh:
    for line in datefh:
        prog, date = line.strip().split(',')
        prog_dates[prog] = date

## now have a dictionary
print(prog_dates)  # REV: still has header information

## TODO: read in and merge version information and output to new file
