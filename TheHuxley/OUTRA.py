dna = []
n = int(input(""))

for i in range(n):
    ref = (input()).upper()
    com = (input()).upper()
    cont = len(ref)

    for j in range(cont):
        if ref[j] == 'G':
            dna.append('c')
        if ref[j] == 'C':
            dna.append('G')
        if ref[j] == 'A':
            dna.append('T')
        if ref[j] == 'T':
            dna.append('A')
    if com == ''.join(dna):
        print('COMṔLEMENTARES')
    else:
        print('NÃO COMPLEMENTARES')
        print(''.join(dna))
    dna = []  