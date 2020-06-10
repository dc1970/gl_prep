#!/usr/local/bin/python3
# Collect annotation errors

irun_log = 'irun_comp.stat_log'
annotate_log = 'arbel_top_taa0.sdf.X_sdf_annotation.log'

irun_file = open(annotate_log, 'r')
annotate_file = open(annotate_log, 'r')
outfile = open('annotation_erros.txt', 'w')

err_list = []
errs_dict= {}

for line in annotate_file:
    if '*W,' in line:
        err_type = line.split()[1]
        err_type = err_type[3:-1]
        if err_type not in err_list:
            err_list.append(err_type)
            errs_dict[err_type] = []
            print(err_type)
        errs_dict[err_type].append(line)

for typ in err_list:
    print('Start report: {} Total errors: {}\n'.format(typ, len(errs_dict[typ])))
    outfile.write('\nStart report: {} Total errors: {}\n'.format(typ, len(errs_dict[typ])))
    outfile.write('---------------------------------------\n')
    for warn in errs_dict[typ]:
        outfile.write(warn+'\n')