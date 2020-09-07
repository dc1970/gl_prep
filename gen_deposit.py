#Get two files of uninlized cells: for FF and fo


eck_file = open('PREICG_06Sep.rpt', 'r').read().splitlines()
q_file = open('latch_06Sep.rpt', 'r').read().splitlines()
#flops_file = open('flops.txt', 'r').read().splitlines()
outfile = open('uninitialized_cells_gl.list', 'w')

for line in eck_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.ECK\n'
    outfile.write(line)

for line in q_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.Q\n'
    outfile.write(line)

#for line in flops_file:
#    line = line.split()  #REmove the cell name from the line
#    line[0] = line[0].replace('/', '.')
#    line[0] = 'dut.' + line[0] + '.Q\n'
#    outfile.write(line[0])