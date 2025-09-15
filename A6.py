def grande(x,y):
    if x>y:
        print(f'\n{x}\n')
    elif x<y:
        print(f'\n{y}\n')
    else:
        print('\nSão iguais\n')
if __name__=='__main__':
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    maior = grande(num1, num2)
    num3 = int(input('Terceiro número: '))
    num4 = int(input('Quarto número: '))
    maior1 = grande(num3, num4)

