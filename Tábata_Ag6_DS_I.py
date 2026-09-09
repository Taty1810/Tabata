# ------------------------------------------------------------------
# PROGRAMA DE DESCONTO PROGRESSIVO - LOJA ONLINE
# ------------------------------------------------------------------

# Entrada de dados: Solicita o valor da compra e converte para decimal (float)
valor_compra = float(input("Digite o valor total da compra: R$"))

# Estrutura condicional para definir o percentual de desconto
if valor_compra < 200.00:
    percentual_desconto = 0.05  # 5% de desconto para compras menores que R$ 200
elif valor_compra < 300.00:
    percentual_desconto = 0.10  # 10% de desconto para compras entre R$ 200 e R$ 299.99
else:
    percentual_desconto = 0.15  # 15% de desconto para compras a partir de R$ 300

# Cálculos dos valores de desconto e o total final
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# Exibição dos resultados formatados com duas casas decimais
print("\n=======================================")
print("          RESUMO DO DESCONTO           ")
print("=======================================")
print(f"Valor original:   R$ {valor_compra:.2f}")
print(f"Desconto ({int(percentual_desconto * 100)}%):  R$ {valor_desconto:.2f}")
print("---------------------------------------")
print(f"Total a pagar:    R$ {valor_final:.2f}")
print("=======================================")
