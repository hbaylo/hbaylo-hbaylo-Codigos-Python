num1 = float(input("primeira nota: "))
num2 = float(input("segunda nota: "))
media = (num1 + num2)/2
print(f'\nmedia:{media:.2f}')
if media >= 5:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")