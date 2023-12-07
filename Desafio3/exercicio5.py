meus_numeros = [6,3,32,12,5,10,74,13,41,22,9,37]

lista_numeros_pares = [numero for numero in meus_numeros if numero % 2 == 0]
print (f'Os números pares da lista são {lista_numeros_pares}.')
numeros_maiores_que_20 = []
numeros_menores_que_20 = []

for numero in meus_numeros:
    if numero > 20:
        numeros_maiores_que_20.append(numero)
    elif numero < 20:
        numeros_menores_que_20.append(numero)

print (f' Esses são os números maiores que 20: {numeros_maiores_que_20}')
print (f' Esses são os números menores que 20: {numeros_menores_que_20}')