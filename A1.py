def soma_dois (x,y):
    soma = x + y
    return soma
if __name__ =='__main__':
    num1 = int(input("Primeiro valor: "))
    num2 = int(input("Segundo valor: "))
    resultado = soma_dois(num1, num2)
    print("resultado: ",resultado)
    resultado1 = soma_dois(2.1, 3.5)
    print("resultado: ", resultado1)