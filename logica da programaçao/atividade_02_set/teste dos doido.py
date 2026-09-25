def calcular_preco_final(preco_original, desconto_percentual):
    valor_desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - valor_desconto
    return preco_final, valor_desconto

preco_prod = float(input("Digite o preço do produto (R$): "))
porcentagem = float(input("Digite o desconto (%): "))
preco_com_desconto, economia = calcular_preco_final(preco_prod, porcentagem)
print(f"\nResumo da compra:")
print(f"Você economizou: R$ {economia:.2f}")
print(f"Preço final a pagar: R$ {preco_com_desconto:.2f}")
#def ="definir"