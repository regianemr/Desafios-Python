import csv

membros = 'Desafio5/membrosC.csv'
with open (membros, 'r') as arquivo:
        leitor_csv = csv.reader (arquivo)
        next(leitor_csv)
        for linha in leitor_csv:
            print(linha)
