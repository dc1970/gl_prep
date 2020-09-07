# Convert lists of cells to system Verilog deposit

list_file = open('uninitialized_cells_gl.list', 'r').read().splitlines()
outfile = open('deposit.inc', 'w')

#outfile.write("module deposit;\n")
outfile.write("initial begin\n")
for line in list_file:
    outfile.write("$deposit (dte_board_taa0." + line + ", 1'b0);\n")

outfile.write("end\n")
# outfile.write("endmodule\n")