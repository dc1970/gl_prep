
sync_list_file = open('synchronizers.txt', 'r')
tfile = open('arbel.tfile', 'w')
sync_lines = sync_list_file.readlines()

# Add base path
tfile.write('BASENAME dte_board_taa0.dut\n')
lines_counter = 0

for l in sync_lines:
    for line in l.split():
        lines_counter += 1
        # 1) ADD "PATH" in the begging  "-tcheck" at the end
        line = 'PATH ' + line.strip() + ' -tcheck\n'

        # 2) replace strings
        line = line.replace('[', '_')
        line = line.replace(']', '_')
        line = line.replace('.', '_')
        line = line.replace('__', '_')
        line = line.replace('/', '.')

        tfile.write(line)

print('Totla num of line: ', lines_counter)

tfile.close()
sync_list_file.close()