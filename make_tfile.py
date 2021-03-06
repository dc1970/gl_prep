sync_list_file = open('synchronizers.txt', 'r')
tfile = open('arbel.tfile', 'w')
sync_lines = sync_list_file.readlines()

# Remove base path and add it to ech line ..
#tfile.write('BASENAME dte_board_taa0.dut\n') ..
lines_counter = 0

for l in sync_lines:
    for line in l.split():  # There are 3 in synchronizer paths in each line
        lines_counter += 1
        # 1) ADD "PATH" in the begging  "-tcheck" at the end
        line = 'PATH dte_board_taa0.dut.' + line.strip() + ' -tcheck\n'

        # 2) replace strings
        line = line.replace('[', '_')
        line = line.replace(']', '_')
        line = line.replace('.', '_')
        line = line.replace('__', '_')
        line = line.replace('/', '.')
        line = line.replace('dte_board_taa0_dut_', 'dte_board_taa0.dut.')

        tfile.write(line)

print('Total num of line: ', lines_counter)

tfile.close()
sync_list_file.close()
