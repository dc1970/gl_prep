
sync_list_file = open('synchronizers.txt', 'r')
tfile = open('arbel.tfile', 'w')
sync_lines = sync_list_file.readlines()

# Add base path
tfile.write('BASENAME dte_board_taa0.dut\n')
counter = 0

for line in sync_lines:
    # 1) ADD "PATH" in the begging  "-tcheck" at the end
    line = 'PATH ' + line.strip() + ' -tcheck\n'

    # 2) replace [<num>] with _<num>_
    line = line.replace('[', '_')
    line = line.replace(']', '_')

    # 3) Replace space with '.'
    new_line = ''
    for i in range(len(line)):
        if line[i-1:i+1] == '_ ' and line[i:i+2] != ' -':
            counter += 1
            new_line = new_line + '.'
        else:
            new_line = new_line + line[i]

    tfile.write(new_line)

print('Num of change: ', counter)

tfile.close()
sync_list_file.close()