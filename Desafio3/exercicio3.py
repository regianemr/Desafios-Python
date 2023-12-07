nome_comediante = "Afonso Padilha"
tem_espaco = False

# for caractere in nome_comediante:
#     if caractere.isspace():
#         tem_espaco = True

tem_espaco = ' ' in nome_comediante
if tem_espaco:
    print(f'O nome {nome_comediante} tem espaços em bancro.')
else:
    print(f'O nome {nome_comediante} não possui espaços em branco.')

nome_comediante_minusculas = nome_comediante.lower()
nome_comediante_maiuscula = nome_comediante.upper()
print(nome_comediante_minusculas)
print(nome_comediante_maiuscula)

letras_a_serem_contadas = 'a'
contagem = nome_comediante_minusculas.count(letras_a_serem_contadas)
print(f'No nome {nome_comediante} tem {contagem} letras {letras_a_serem_contadas}.')