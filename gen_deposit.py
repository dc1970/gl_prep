#Get two files of uninlized cells: for FF and fo


eck_file = open('PREICG', 'r').read().splitlines()
q_file = open('latches.txt', 'r').read().splitlines()
outfile = open('uninitialized_cells_gl.list', 'w')

for line in eck_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.ECK\n'
    #if 'byte_lane_0__lane_side_dfi_phy___dfi_phy_l' in line:
    #    line = line.replace('dfi_phy_l.','dfi_phy_l.\\')
    #    line = line.replace('RC_CGIC_INST', '/RC_CGIC_INST')
    outfile.write(line)


for line in q_file:
    line = line.replace('/', '.')
    line = 'dut.' + line + '.Q\n'
    #if 'byte_lane_0__lane_side_dfi_phy___dfi_phy_l' in line:
    #    line = line.replace('dfi_phy_l.','dfi_phy_l.\\')
    #    line = line.replace('RC_CGIC_INST', '/RC_CGIC_INST')
    outfile.write(line)