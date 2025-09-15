"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Elabore o programa que gere a sequência dos números naturais ímpares até 13.

- Passos para resolver o problema (algoritmo):

escreva cabeçalho
for variavel_for in range(v_inicial, v_final, v_passo):
    escreva variavel_for
escreva mensagem

- Teste:

Saída:
- Números ímpares:
1
3
5
...
13
"""
print('- Números ímpares:')                 # Cabeçalho.
for impar in range(1, 13+1, 2):             # for impar in range(1, 14, 2):
    print(impar)





''' ----- ALTERAÇÕES:
a. Mostre a quantidade de valores gerados, use contador. Saída: Quantidade = 7
b. Mostre a soma dos valores da sequência, use somador.  Saída: Soma = 49
c. Refaça o exercício usando o passo 1.
d. Utilize a mesma ideia (de saltos de 2 elementos) para substituir o for por
   um while equivalente.                                          
   ----- DICAS ABAIXO:
ct = 0                          # Antes do for                  # a.
    ct = ct + 1                 # Dentro do for, indentado
print("Quantidade =", ct)       # Depois do for
soma = 0                        # Antes do for                  # b.
    soma = soma + impar         # Dentro do for, indentado
print ("Soma = ", soma)         # Depois do for         
for i in range(0, 13 + 1, 1):                                   # c.
    if i % 2 != 0:    # if i % 2 == 1:    # se i é impar
        print(i)                              
contador = 1                                                    # d.
while(contador <= 13)
    print(i)
    contador += 2
                                    
'''
