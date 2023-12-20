
class Aluno:
    def __init__(self, nome, sobrenome, cadastro, frequencia):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cadastro = cadastro
        self.frequencia = frequencia

    def __str__(self):
        return f"{self.nome} {self.sobrenome}, cadastrado em {self.cadastro}, frequência: {self.frequencia}"  
       
    def __repr__(self):
        return f"{self.nome} {self.sobrenome}, cadastrado em {self.cadastro}, frequência: {self.frequencia}"  