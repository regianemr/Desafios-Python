nomes_alunos = ["Marcos", "Ana", "Jeferson", "Eduardo", "Lucas", "Ivo",
"Pedro"]
nomes_com_mais_de_5_letras = []

for nome in nomes_alunos:
    if len(nome) > 5:
        nomes_com_mais_de_5_letras.append(nome)
print (f'Nomes na lista com mais de 5 letras: {nomes_com_mais_de_5_letras}.')