
import csv
from datetime import datetime

membros = 'Desafio2/membros.csv'
with open(membros, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    data_cadastro_mais_antigo = None
    
    for cadastro in leitor_csv:
        data_cadastro = cadastro [3]
        data = datetime.strptime(data_cadastro, '%Y-%m-%d')

        if data_cadastro_mais_antigo is None:
            data_cadastro_mais_antigo = data
            nome_aluno = cadastro[1] 
        elif data < data_cadastro_mais_antigo:
            data_cadastro_mais_antigo = data
            nome_aluno = cadastro[1] 
        
        
    print (f" O aluno com o cadastro mais antigo foi {nome_aluno} em {data_cadastro_mais_antigo.strftime('%Y-%m-%d')}")
    
 # for cadastro in leitor_csv:
    #     cadastro_texto = cadastro[3]
    #     data = datetime.strptime(cadastro_texto, '%Y-%m-%d')
    #     datas.append(data)
# cadastro_mais_antigo = min(datas)
# cadastro_mais_novo = max(datas)
# print (f" O aluno com o cadastro mais antigo foi {nome_aluno} em {cadastro_mais_antigo.strftime('%Y-%m-%d')} e o mais novo em:{cadastro_mais_novo.strftime('%Y-%m-%d')}")
    # data_cadastro_mais_antigo = None

    # for cadastro in leitor_csv:  
    #     data_cadastro = cadastro[3]

    #     if data_cadastro_mais_antigo is None:
    #         data_cadastro_mais_antigo = data_cadastro
    #         nome_aluno = cadastro[1]
    #     elif data_cadastro < data_cadastro_mais_antigo:
    #         data_cadastro_mais_antigo = data_cadastro
    #         nome_aluno = cadastro[1]

    # print (f' O(a) aluno(a) {nome_aluno} se cadastrou na data: {data_cadastro_mais_antigo}, sendo o aluno(a) mais antigo.')

