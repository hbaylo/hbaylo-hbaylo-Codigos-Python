def grande(x,y):
    if x>y:
        print(f'\n{x}\n')
    elif x<y:
        print(f'\n{y}\n')
    else:
        print('\nSão iguais\n')
def menor(z,c):
    if z<c:
        print(f'\n{z}')
    elif z>c:
        print(f'\n{c}')
    else:
        print('\nSão iguais')
if __name__=='__main__':
    print(' MAIOR NÚMERO ')
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    grande(num1, num2)
    print(' MENOR NÚMERO ')
    num3 = int(input('Primeiro número: '))
    num4 = int(input('Segundo número: '))
    menor(num3, num4)