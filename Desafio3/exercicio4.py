meus_numeros = [6,3,32,12,5,10,74,13,41,22,9,37]

lista_numeros_pares = [numero for numero in meus_numeros if numero % 2 == 0]
print (f'Os números pares da lista são {lista_numeros_pares}.')
lista_numeros_impares = []

for numero in meus_numeros:
    if numero % 2 != 0:
        lista_numeros_impares.append(numero)  

print (f'Os números ímpares da lista são {lista_numeros_impares}.')
       