import csv 
from fittech.academia import Academia

membros = 'Desafio5/membrosC.csv'

AcademiaC = Academia('Academia C', 'Rua C')
AcademiaC.carregar_alunos(membros)
print(AcademiaC.alunos_maior_frequencia())
print(AcademiaC.alunos_menor_frequencia())
print(AcademiaC)