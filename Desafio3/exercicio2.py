nome_comediante = "Afonso Padilha"
primeira_letra_do_nome = nome_comediante[0].lower()
vogais = ['a', 'e', 'i','o', 'u']

if primeira_letra_do_nome in vogais:
    print(f'A primeira letra do nome {nome_comediante} é uma vogal.')

else:
    print('A primeira letra do nome é uma consoante.')

    