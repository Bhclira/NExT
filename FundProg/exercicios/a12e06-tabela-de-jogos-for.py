# Desenvolva um programa que possa gerar a tabela de jogos do campeonato
# brasileiro para 4 times (times jogam em casa e na casa do adversário).
# Times: Flamengo, São Paulo, Fluminense, Palmeiras.
# Saída de dados: Flamengo x São Paulo
# Flamengo x Fluminense
# Flamengo x Palmeiras
# São Paulo x Flamengo

for time1 in ("Flamengo", "São Paulo", "Fluminense", "Palmeiras"):
    for time2 in ("Flamengo", "São Paulo", "Fluminense", "Palmeiras"):
        if time1!=time2:
            print(time1, 'x', time2)