def soma_dois (x,y):
    return x + y
def menos_dois (z,c):
    return z - c
if __name__ =='__main__':
    modo = int(input("Somar - digite 1, Subitrair - digite 2.: "))
    if modo == 1:
     num1 = int(input("Primeiro número: "))
     num2 = int(input("Segundo número: "))
     resultado1 = soma_dois(num1, num2)
     print("Primeiro resultado: ", resultado1)
    elif modo == 2:
     num3 = int(input("Primeiro número: "))
     num4 = int(input("Segundo número: "))
     resultado2 = menos_dois(num3, num4)
     print("Segundo resultado: ", resultado2)
    else:
        print("Opção invalida")
