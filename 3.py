ct = 0
soma = 0
print('-Numeros naturais na vertical: ')
for i in range(1, 13, 2):
    print(i)
    ct = ct + 1
    soma += i
    "Pode ser tanto com soma += i , como soma = soma + i"
print('Encerrou a repetição')
print(f'Quantidade: {ct}')
print(f'Soma = {soma}')