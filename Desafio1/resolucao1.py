import csv

alunos = 'Desafio1/alunos.csv'
with open(alunos, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)

    for aluno in leitor_csv:
        nota_aluno = int(aluno[2])
        if nota_aluno < 6:
            print(f'Aluno {aluno[0]} reprovado')
        else:
            print(f'Aluno {aluno[0]} aprovado')
