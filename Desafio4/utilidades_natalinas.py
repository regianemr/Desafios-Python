import random

# def filtra_criancas_bem_comportadas(criancas):
#     criancas_bem_comportadas = [crianca for crianca in criancas if crianca['comportada']] 
#     return criancas_bem_comportadas

# def filtra_criancas_nao_comportadas(criancas):
#     criancas_nao_comportadas = [crianca for crianca in criancas if not crianca['comportada']] 
#     return criancas_nao_comportadas

def filtrar_criancas(criancas, comportadas=True):
        return [crianca for crianca in criancas if crianca['comportada'] == comportadas] 
    
def sortear_crianca_bem_comportada(criancas):
    criancas_bem_comportadas = [crianca for crianca in criancas if crianca['comportada']]
    if criancas_bem_comportadas:
        crianca_sorteada = random.choice(criancas_bem_comportadas)
        return crianca_sorteada
    else:
        return None

