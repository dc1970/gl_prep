# Remove all cells in cell_err.txt from uninitialized_cells_gl_orig.list
# and save it in uninitialized_cells_gl.list

cells_file = open('uninitialized_cells_gl_orig.list', 'r').read().splitlines()
errs_file = open('cell_err.txt', 'r').read().splitlines()
outfile = open('uninitialized_cells_gl.list', 'w')

err_nb = 0
cell_nb = 0
for line in cells_file:
    if line in errs_file:
        print(line)
        err_nb += 1
    else:
        outfile.write(line)
        cell_nb += 1

print('Correct cells: {}, Error cells: {}'.format(cell_nb, err_nb))
