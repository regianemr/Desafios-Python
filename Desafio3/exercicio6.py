nomes_alunos = ["Marcos", "Ana", "Jeferson", "Eduardo", "Lucas", "Ivo",
"Pedro"]
vogais = 'aeiouAEIOU'
nomes_que_comecam_vogais = []
nomes_que_finalizam_vogais = []
nomes_inicio_consoante = []
nomes_fim_consoante = []

for nome in nomes_alunos:
    if nome[0] in vogais:
        nomes_que_comecam_vogais.append(nome)
    if nome[-1] in vogais:
        nomes_que_finalizam_vogais.append(nome)
    if nome[0] not in vogais:
        nomes_inicio_consoante.append(nome)
    if nome[-1] not in vogais:
        nomes_fim_consoante.append(nome)

print (f'Esses são os nomes que começam com vogais: {nomes_que_comecam_vogais}.')
print (f'Esses são os nomes que finalizam com vogais: {nomes_que_finalizam_vogais}.')
print (f'Esses são os nomes que iniciam com consoantes: {nomes_inicio_consoante}.')
print (f'Esses são os nomes que finalizam com consoantes: {nomes_fim_consoante}.')

