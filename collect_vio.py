#!/usr/local/bin/python3
# List all timing violaton from log file

log_file = open('run/irun.stat_log', 'r')
vio_set = set([])

for line in log_file:
    if 'Scope:' in line:
        line = line.split()[1]
        vio_set.add(line)
for line in vio_set:
    print(line)
