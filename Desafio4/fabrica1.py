from utilidades_natalinas import filtrar_criancas, sortear_crianca_bem_comportada

criancas_natal = [
    { "nome": "Livvyy", "sobrenome": "Poppy", "comportada": False },
    { "nome": "Tamqrah", "sobrenome": "Thunell", "comportada": False },
    { "nome": "Cissiee", "sobrenome": "Han", "comportada": False },
    { "nome": "Cyndie", "sobrenome": "Dominy", "comportada": True },
    { "nome": "Heddie", "sobrenome": "Franza", "comportada": False },
    { "nome": "Paule", "sobrenome": "Fabiola", "comportada": False },
    { "nome": "Mildrid", "sobrenome": "Rosalba", "comportada": False },
    { "nome": "Eve", "sobrenome": "Bearnard", "comportada": False },
    { "nome": "Charissa", "sobrenome": "Marden", "comportada": True },
    { "nome": "Sheelagh", "sobrenome": "Tufts", "comportada": True },
    { "nome": "Beverley", "sobrenome": "Rustice", "comportada": False },
    { "nome": "Nananne", "sobrenome": "Jacqui", "comportada": True },
    { "nome": "Wileen", "sobrenome": "Stilwell", "comportada": True },
    { "nome": "Coral", "sobrenome": "Boycey", "comportada": False },
    { "nome": "Eadie", "sobrenome": "Aldric", "comportada": False },
    { "nome": "Nannie", "sobrenome": "Westphal", "comportada": True },
    { "nome": "Marcelline", "sobrenome": "Juan", "comportada": False },
    { "nome": "Louella", "sobrenome": "Vernier", "comportada": True },
    { "nome": "Leanna", "sobrenome": "Morehouse", "comportada": False },
    { "nome": "Clarice", "sobrenome": "Kosey", "comportada": True },
    { "nome": "Jinny", "sobrenome": "Fiann", "comportada": True },
    { "nome": "Gratia", "sobrenome": "Kauppi", "comportada": True },
    { "nome": "Ulrike", "sobrenome": "Braun", "comportada": False },
    { "nome": "Letizia", "sobrenome": "Gabrielli", "comportada": False},
    { "nome": "Korrie", "sobrenome": "Velick", "comportada": True },
]

# criancas_comportadas = filtra_criancas_bem_comportadas(criancas_natal)
# print(criancas_comportadas)


# criancas_nao_comportadas = filtra_criancas_nao_comportadas(criancas_natal)
# print(criancas_nao_comportadas)

crianca_sorteada = sortear_crianca_bem_comportada(criancas_natal)
if crianca_sorteada:
    print(f"Criança sorteada: {crianca_sorteada['nome']} {crianca_sorteada[ 'sobrenome']}")
else:
    print ('Não existe crianças sorteadas comportadas.')
    
# criancas_bem_comportadas = filtra_criancas_bem_comportadas(criancas_natal)
# for crianca in criancas_bem_comportadas:
#     print(f" {crianca['nome']} {crianca['sobrenome']}")

# criancas_nao_comportadas = filtra_criancas_nao_comportadas(criancas_natal)
# for crianca in criancas_nao_comportadas:
     
    # print(f"{crianca['nome']} {crianca['sobrenome']}")

bem_comportadas = filtrar_criancas(criancas_natal)
nao_comportadas = filtrar_criancas(criancas_natal, comportadas=False)

for crianca in bem_comportadas:
    print(f"{crianca['nome']} {crianca['sobrenome']}")

for crianca in nao_comportadas:
    print(f"{crianca['nome']} {crianca['sobrenome']}")