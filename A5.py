def grande(x,y):
    if x>y:
        print(f'\n{x}')
    elif x<y:
        print(f'\n{y}')
    else:
        print('\nSão iguais')
if __name__=='__main__':
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    maior = grande(num1, num2)