class Funcionario:
    def __init__(self, nome, identidade, setor, salario):
        self.nome = nome
        self.identidade = identidade
        self.setor = setor
        self.salario = salario

    def __repr__(self):
        return '(' + str(self.nome) + ' ,' + str(self.identidade) + ' ,' + str(self.setor) + ' ,' + str(self.salario) + ','

class Gerente(Funcionario):

    def __repr__(self):
        return '(' + str(self.nome) + ' ,' + str(self.identidade) + ' ,' + str(self.setor) + ' ,' + str(self.salario + self.salario * 0.15) + ','