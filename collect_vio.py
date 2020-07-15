#!/usr/local/bin/python3
# List all timing violaton from log file
import sys
import os

#Help
if len(sys.argv) != 2:
    print('\n\n Syntax: \n')
    print('\t collect_vios <log file>\n')
    exit()

# Check if file exists
if not os.path.isfile(sys.argv[1]):
    print('\n\tFile: ', sys.argv[1], 'Does not exists\n')
    exit()

log_file = open('run/irun.stat_log', 'r')
vio_set = set([])
before_reset = True

for line in log_file:
    if 'Drive strap pins of reset VSB_RESET' in line and before_reset:
        before_reset = False
    else:
        continue
    if 'Scope:' in line and 'gfx_core' not in line:
        line = line.split()[1]
        vio_set.add(line)
for line in vio_set:
    print(line)
