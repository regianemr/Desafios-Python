import csv

membros = 'Desafio2/membros.csv'
with open (membros, 'r') as arquivo:
    leitor_csv = csv.reader (arquivo)
    next(leitor_csv)

    numero_mensalidade = 1
    numero_aluno_homem_deve = 0
    numero_aluno_mulher_deve = 0

    for membro in leitor_csv:
        mensalidades_atrasadas = int(membro[5])
        sexo_aluno = membro[4]
        
        if mensalidades_atrasadas >= numero_mensalidade and sexo_aluno == 'm':
            numero_aluno_homem_deve +=1
        elif mensalidades_atrasadas >= numero_mensalidade and sexo_aluno == 'f':
            numero_aluno_mulher_deve +=1

    print(f'Temos {numero_aluno_homem_deve} homens devendo') 
    print(f'Temos {numero_aluno_mulher_deve} mulheres devendo')
     