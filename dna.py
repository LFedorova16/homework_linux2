import sys
if len(sys.argv) < 2:
    print("Использование: ./dna.py <последовательность>")
    sys.exit(1)
dna = sys.argv[1]
compl_map = str.maketrans("ATGC", "TACG")
compl = dna.translate(compl_map)
reverse_compl = compl[::-1]
rna = reverse_compl.replace("T", "U")
start_k = dna.find("ATG")
print(dna, "->", reverse_compl, rna, start_k)
