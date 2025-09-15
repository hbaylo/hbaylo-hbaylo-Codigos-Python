class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def get_modelo(self):
        return self.modelo
    def get_ano(self):
        return self.ano
    def get_valor(self):
        return self.valor
    def set_modelo(self,novo_modelo):
        self.modelo = novo_modelo
    def set_ano(self, novo_ano):
            self.ano = novo_ano
    def set_valor(self,novo_valor):
        self.valor = novo_valor
    def aumenta_valor(self,valor_aumento):
        self.valor = self.valor + valor_aumento

if __name__=='__main__':
    carro1 = Veiculo('HB20', 2022, 80000.00)
    print("\nEndereço hexadecimal do Carro 1: ", carro1)
    print("Modelo carro 1: ",carro1.get_modelo())
    print("Ano carro 1: ", carro1.get_ano())
    print("Valor carro 1: ", carro1.get_valor())
    print("\nNovo Modelo", carro1.get_modelo())
    carro2 = Veiculo('Corolla', 2024, 190000.00)
    print("\nEndereço hexadecimal do Carro 2: ", carro2)
    print("Modelo carro 2: ", carro2.get_modelo())
    print("Ano carro 2: ", carro2.get_ano())
    print("Valor carro 2: ", carro2.get_valor())
    print('----------------------------------------------------------')
    mudança = input("Precisa mudar algo? (Escreva sim ou não): ")
    if mudança == 'sim':
        print("Alteração de dados:")
        print('----------------------------------------------------------')
        Usuario_Modelo1 = input("Escreve o novo modelo para o carro 1: ")
        Usuario_Ano1 = int(input("Escreve o novo ano para o carro 1: "))
        Usuario_Valor1 = float(input("Escreve o novo valor para o carro 1: "))
        print('----------------------------------------------------------')
        carro1.set_modelo(Usuario_Modelo1)
        print('Novo Modelo: ',carro1.get_modelo())
        carro1.set_ano(Usuario_Ano1)
        print("Novo ano:",carro1.get_ano())
        carro1.set_valor(Usuario_Valor1)
        print("Novo valor",carro1.get_valor())
        print('----------------------------------------------------------')
        Usuario_Modelo2 = input("Escreve o novo modelo para o carro 2: ")
        Usuario_Ano2 = int(input("Escreve o novo ano para o carro 2: "))
        Usuario_Valor2 = float(input("Escreve o novo valor para o carro 2: "))
        print('----------------------------------------------------------')
        carro2.set_modelo(Usuario_Modelo2)
        print('Novo Modelo: ', carro2.get_modelo())
        carro2.set_ano(Usuario_Ano2)
        print("Novo ano:", carro2.get_ano())
        carro2.set_valor(Usuario_Valor2)
        print("Novo valor", carro2.get_valor())
        print('----------------------------------------------------------')
        mudança1 = input("Precisa aumentar o preço? (Escreva sim ou não): ")
        if mudança1 =='sim':
            print('----------------------------------------------------------')
            valor_aumento1 = float(input("Escreva o aumento no valor do carro 1: R$ "))
            carro1.aumenta_valor(valor_aumento1)
            print("Valor aumentado do carro 1: R$ ",carro1.get_valor())
            print('----------------------------------------------------------')
            valor_aumento2 = float(input("Escreva o aumento no valor do carro 2: R$ "))
            carro2.aumenta_valor(valor_aumento2)
            print("Valor aumentado do carro 2: R$ ", carro2.get_valor())
        else:
            print("\nCódigo finalizado")
    else:
        print("\nCódigo finalizado")
