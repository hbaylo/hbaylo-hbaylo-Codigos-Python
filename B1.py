class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
if __name__=='__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    print("Endereço hexadecimal do aluno 1: ", aluno1)
    aluno2 = Aluno('Emily', 1300.00, 17)
    print("Endereço hexadecimal do aluno 2: ", aluno2)

