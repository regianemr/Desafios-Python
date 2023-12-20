import csv 
from fittech.academia import Academia

membros = 'Desafio5/membrosA.csv'

academiaA = Academia('Academia A', 'Rua A')
academiaA.carregar_alunos(membros)
print(academiaA.alunos_maior_frequencia())
print(academiaA.alunos_menor_frequencia())
print(academiaA)