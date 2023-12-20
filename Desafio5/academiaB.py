import csv 
from fittech.academia import Academia

membros = 'Desafio5/membrosB.csv'

academiaB = Academia('Academia B', 'Rua B')
academiaB.carregar_alunos(membros)
print(academiaB.alunos_maior_frequencia())
print(academiaB.alunos_menor_frequencia())
print(academiaB)
print(academiaB.alunos)