ct = 0
soma = 0
inicial = int(input("Primeiro numero: "))
final = int(input("Ultimo numero: "))
for i in range(inicial, final+1, 1):
    print(i)
    ct = ct + 1
    soma += i
print('Encerrou a repetição')
print(f'Quantidade: {ct}')
print(f'Soma = {soma}')