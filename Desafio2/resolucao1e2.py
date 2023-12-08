import csv

membros = 'Desafio2/membros.csv'
with open (membros, 'r') as arquivo:
    leitor_csv = csv.reader (arquivo)
    next(leitor_csv)

    max_mensalidade_atraso = 1

    for membro in leitor_csv:
        mensalidades_atrasadas = int(membro[5])
        nome_aluno = membro[1]
    
        if mensalidades_atrasadas == max_mensalidade_atraso:
            print(f'O aluno {nome_aluno} está devendo uma mensalidade, por favor entre em contato com a gerência.')
        
        elif mensalidades_atrasadas > max_mensalidade_atraso:
            print(f'O aluno {nome_aluno} está devendo MAIS DE UMA mensalidade, estando perto de ser expulso.')


