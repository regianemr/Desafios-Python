import csv

membros = 'Desafio2/membros.csv'
with open(membros, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv) #para pular cabeçalho
    numero_mensalidade_atrasada = 1
    numero_frequencia_aluno = 3
    quantidade_aluno_devendo = 0
    quantidade_aluno_frenquencia_igual_zero = 0

    for aluno in leitor_csv:
        frequencia_aluno = int(aluno[6])
        numero_aluno = int(aluno[0])
        mensalidade_atrasada = int(aluno[5])
    
        if frequencia_aluno > numero_frequencia_aluno and mensalidade_atrasada >= numero_mensalidade_atrasada:
            quantidade_aluno_devendo +=1
        if frequencia_aluno == 0:
            quantidade_aluno_frenquencia_igual_zero +=1 
            
    print (f'Temos {quantidade_aluno_devendo} alunos com a frequência maior que 3 e estão devendo, e  {quantidade_aluno_frenquencia_igual_zero} alunos com a frequência igual a zero.')
            

    


               
        

