"""Merge program info by program name

usage: merge_program_info.py

REV: how could this script be generalized?
"""
from collections import defaultdict

dates_file = '../../data/program-dates.csv'
version_file = '../../data/program-versions.csv'

# prog_dates = {}  # dictionary of dates keyed by program name
proginfo = defaultdict(list)

with open(dates_file) as datefh:
    for line in datefh:
        prog, date = line.strip().split(',')
        proginfo[prog].append(date)

## now have a dictionary
#print(prog_dates)  # REV: still has header information

## TODO: read in and merge version information and output to new file
with open(version_file) as versionfh:
    for line in versionfh:
        prog, version = line.strip().split(',')
        proginfo[prog].append(version)


print(proginfo.items())
