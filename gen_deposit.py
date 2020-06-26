#Get two files of uninlized cells: for FF and fo


eck_file = open('PREICG', 'r').read().splitlines()
q_file = open('latches.txt', 'r').read().splitlines()
flops_file = open('flops.txt', 'r').read().splitlines()
outfile = open('uninitialized_cells_gl.list', 'w')

for line in eck_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.ECK\n'
    outfile.write(line)

for line in q_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.Q\n'
    outfile.write(line)

for line in flops_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.Q\n'
    outfile.write(line)