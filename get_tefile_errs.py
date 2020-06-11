# Print all the errors related to tfile

log_file = open('irun_comp.stat_log', 'r')
log_lines = log_file.readlines()
out_file = open('tfile_errs.txt', 'w')

counter = 0
for line in log_lines:
    if 'TFANOTU' in line:
        out_file.write(line.split()[6][19:])
        counter += 1

print('Update tfile_errs.txt - total errors: ', counter)
out_file.close()
