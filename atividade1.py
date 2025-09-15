num1 = float(input("primeira nota: "))
num2 = float(input("segunda nota: "))
num3 = float(input("terceira nota: "))
media = (num1 + num2 + num3)/3
print(f'\nmedia:{media:.2f}')
if media >= 5:
    print("aprovado")
else:
    print("\nfazer recuperação!!!")
    recuperacao = 10 - media
    print(f'nota nescessaria para a recuperacao: {recuperacao:.2f}')
    num4 = float(input("\nnota da recuperação: "))
    if num4 >= recuperacao:
        print("\naprovado")
    else:
        print("\nreprovado")
