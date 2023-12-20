import csv
from fittech.aluno import Aluno


class Academia:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.alunos = []

    def __str__(self):
        return 'olá' 

    def carregar_alunos(self, caminho_arquivo):
        with open (caminho_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv)
            for linha in leitor_csv:
                aluno = Aluno(linha[0], linha[1], linha[2], int(linha[3]))
                self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    def alunos_maior_frequencia(self):
        maior_frequencia = max(self.alunos, key=lambda aluno: aluno.frequencia).frequencia
        return [aluno for aluno in self.alunos if aluno.frequencia == maior_frequencia]

    def alunos_menor_frequencia(self):
        menor_frequencia = min(self.alunos, key=lambda aluno: aluno.frequencia).frequencia
        return [aluno for aluno in self.alunos if aluno.frequencia == menor_frequencia] 

    def matricular_aluno(self, aluno):
        self.alunos.append(aluno)

    def cancelar_matricula(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f"Matrícula de {aluno.nome} cancelada com sucesso.")
     
    def __str__(self):
        total_alunos = len(self.alunos)
        return f"Academia: {self.nome}, Endereço: {self.endereco}, Total de alunos: {total_alunos}"