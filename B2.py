class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_mensalidade(self):
        return self.mensalidade
    def get_idade(self):
        return self.idade
if __name__=='__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    print("Endereço hexadecimal do aluno 1: ", aluno1.get_nome(),aluno1.get_mensalidade(),aluno1.get_idade())
    aluno2 = Aluno('Emily', 1300.00, 17)
    print("Endereço hexadecimal do aluno 2: ", aluno2.get_nome(),aluno2.get_mensalidade(),aluno2.get_idade())