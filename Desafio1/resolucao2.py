import csv

alunos = 'Desafio1/alunos.csv'
with open(alunos, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)

    nota_minima_aprovados = 6
    aprovados_A = 0
    aprovados_B = 0
    reprovados_A = 0
    reprovados_B = 0
    
    for aluno in leitor_csv:
        if int(aluno[2]) >= nota_minima_aprovados and aluno[1] == '2A':
            aprovados_A += 1      
        elif int(aluno[2]) >= nota_minima_aprovados and aluno[1] == '2B':
            aprovados_B += 1
        elif int(aluno[2]) < nota_minima_aprovados and aluno[1] == '2A':
            reprovados_A += 1
        elif int(aluno[2]) < nota_minima_aprovados and aluno[1] == '2B':
            reprovados_B += 1

    print(f' O número de aprovados é {aprovados_A} da turma 2A')
    print(f' O número de aprovados é {aprovados_B} da turma 2B')
    print(f' O número de reprovados é {reprovados_A} da turma 2A')
    print(f' O número de reprovados é {reprovados_B} da turma 2B')
