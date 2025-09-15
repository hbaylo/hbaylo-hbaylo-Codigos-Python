compra = float(input("Valor da compra: "))
venda = float(input("Valor de venda: "))
if venda - compra > 0:
    print("Teve lucro")
elif venda - compra < 0:
    print("Teve prejuizo")
else:
    print("Os valores são iguais")