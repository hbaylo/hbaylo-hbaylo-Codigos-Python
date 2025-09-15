def soma_dois (x,y):
    return x + y
def menos_dois (z,c):
    return z - c
if __name__ =='__main__':
    modo = int(input("Somar 2 números - digite 1, Subitrair - digite 2, Somar 4 números - digite 3: "))
    if modo == 1:
     num1 = int(input("Primeiro número: "))
     num2 = int(input("Segundo número: "))
     resultado1 = soma_dois(num1, num2)
     print("Resultado soma de 2 números: ", resultado1)
    elif modo == 2:
     num3 = int(input("Primeiro número: "))
     num4 = int(input("Segundo número: "))
     resultado2 = menos_dois(num3, num4)
     print("Resultado subitração: ", resultado2)
    elif modo == 3:
     num5 = int(input("Primeiro número: "))
     num6 = int(input("Segundo número: "))
     num7 = int(input("Terceiro número: "))
     num8 = int(input("Quarto número: "))
     resultado3 = soma_dois(num5, num6)
     resultado4 = soma_dois(num7, num8)
     resultado5 = resultado3 + resultado4
     print('Resultado soma de 4 números', resultado5)
    else:
        print("Opção invalida")
#Se vc não entendeu vc é burro