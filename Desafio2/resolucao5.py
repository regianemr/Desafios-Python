import csv
from datetime import datetime

membros = 'Desafio2/membros.csv'
with open(membros, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    data_cadastro_mais_novo = None
    
    for cadastro in leitor_csv:
        data_cadastro = cadastro [3]
        data = datetime.strptime(data_cadastro, '%Y-%m-%d')

        if data_cadastro_mais_novo is None:
            data_cadastro_mais_novo = data
            nome_aluno = cadastro[1] 
        elif data > data_cadastro_mais_novo:
            data_cadastro_mais_novo = data
            nome_aluno = cadastro[1] 
        
        
    print (f" O aluno com o cadastro mais novo foi {nome_aluno} em {data_cadastro_mais_novo.strftime('%Y-%m-%d')}")