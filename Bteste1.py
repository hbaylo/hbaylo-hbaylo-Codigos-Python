class Aluno:
    def __init__(self, nomeA, mensalidade, idade):
        self.nomeA = nomeA
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nomeA(self):
        return self.nomeA
    def get_mensalidade(self):
        return self.mensalidade
    def get_idade(self):
        return self.idade
class Professor:
    def __init__(self,nomeP, materia, sala):
        self.nomeP = nomeP
        self.materia = materia
        self.sala = sala
    def get_nomeP(self):
        return self.nomeP
    def get_mateira(self):
        return self.materia
    def get_sala(self):
        return self.sala

if __name__=='__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    print("Endereço hexadecimal do aluno 1: ", aluno1)
    print("Informações do Aluno1: ", aluno1.get_nomeA(), aluno1.get_mensalidade(),
          aluno1.get_idade())
    print('\n')
    aluno2 = Aluno('Emily', 1300.00, 17)
    print("Endereço hexadecimal do aluno 1: ", aluno2)
    print("Informações do Aluno2: ", aluno2.get_nomeA(),aluno2.get_mensalidade(),
          aluno2.get_idade())
    print('\n')
    professor1 = Professor('Carlos', 'Banco de dados', 395)
    print("Endereço hexadecimal do professor1: ", professor1)
    print("Informações do Professor1: ", professor1.get_nomeP(),professor1.get_mateira(),
          professor1.get_sala())
    print('\n')
    professor2 = Professor('João', 'POO', 672)
    print("Endereço hexadecimal do professor2: ", professor2)
    print(f'Informações do Professor2: {professor2.get_nomeP()}, {professor2.get_mateira()}, {professor2.get_sala()}')