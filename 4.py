ct = 0
soma = 0
print('-Numeros naturais na vertical: ')
for i in range(7, 0, -1):
    print(i)
    ct = ct + 1
    "Pode ser tanto ct = ct + 1, quanto, ct += 1"
    soma += i
    "Pode ser tanto com soma += i , como soma = soma + i"
print('Encerrou a repetição')
print(f'Quantidade: {ct}')
print(f'Soma = {soma}')