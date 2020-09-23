#Get two files of uninlized cells: for FF and fo


eck_file = open('PREICG.rpt', 'r').read().splitlines()
q_file = open('latch_q.rpt', 'r').read().splitlines()
qn_file = open('latch_qn.rpt', 'r').read().splitlines()

#flops_file = open('flops.txt', 'r').read().splitlines()
outfile = open('deposit.inc', 'w')
outfile.write('initial begin\n')
for line in eck_file:
    line = line.replace('/', '.')
    line = "$deposit (dut." + line + ".ECK, 1'b0);\n"
    outfile.write(line);

for line in q_file:
    line = line.replace('/', '.')
    line = "$deposit (dut." + line + ".Q, 1'b0);\n"
    outfile.write(line)

for line in qn_file:
    line = line.replace('/', '.')
    line = "$deposit (dut." + line + ".QN, 1'b0);\n"
    outfile.write(line)

#for line in flops_file:
#    line = line.split()  #REmove the cell name from the line
#    line[0] = line[0].replace('/', '.')
#    line[0] = 'dut.' + line[0] + '.Q\n'
#    outfile.write(line[0])

outfile.write('end')
