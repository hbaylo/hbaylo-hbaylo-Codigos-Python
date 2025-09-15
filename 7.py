def calcula_dobro(p_valor):
    dobro = p_valor*2
    return dobro
if __name__ == '__main__':
    valor = int(input("Valor inteiro: "))
    v_retornado = calcula_dobro(valor)
    print("valor retornado pela função: ", v_retornado)
    print("Valor retornado pela função: ", calcula_dobro(valor))