'''
O DNA é constituído por dois longos filamentos enrolados um sobre o outro, formando uma estrutura helicoidal.  A estrutura simples do DNA  lembra a espiral de um caderno. Cada uma das cadeias de DNA é constituída por milhares ou mesmo milhões de unidades chamadas nucleotídeos, ligados em sequência.

As duas cadeias de uma molécula de DNA são sempre complementares: um nucleotídeo com timina (T) em uma das cadeias sempre correspondente a um nucleotídeo com adenina (A) na outra cadeia, e vice-versa; um nucleotídeo com citosina (C) em uma das cadeias sempre correspondente a um nucleotídeo com guanina (G) na outra cadeia, e vice e versa.

Escreva um programa que recebe pares de cadeias de DNA. A primeira cadeia serve como referência e a segunda é uma cadeia de teste. Informe como saída se essas cadeias são ou não complementares. Caso não sejam, corrija a segunda cadeia para que ela torne-se complementar da primeira e também imprima a cadeia corrigida na saída.
'''

lista_dna = []

loop = int(input(""))

for index in range(loop):
    ref = (input()).upper()
    com = (input()).upper()
    cont = len(ref)

    for j in range(cont):
        if ref[j] == 'G':
            lista_dna.append('C')
        if ref[j] == 'C':
            lista_dna.append('G')
        if ref[j] == 'A':
            lista_dna.append('T')
        if ref[j] == 'T':
            lista_dna.append('A')
    if com == ''.join(dna):
        print('COMṔLEMENTARES')
    else:
        print('NÃO COMPLEMENTARES')
        print(''.join(dna))
    dna = []  