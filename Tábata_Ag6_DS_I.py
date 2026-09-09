# =========================================================
# PROGRAMA: Cálculo de Desconto Progressivo por Compra
# AUTORA: Tábata Lima
# DISCIPLINA: Desenvolvimento de Software I
# =========================================================

# --- ENTRADA DE DADOS ---
# Solicita ao usuário o valor da compra e converte para decimal (float)
valor_compra = float(input("Digite o valor total da compra: R$ "))

# --- ESTRUTURA CONDICIONAL (REGRAS DE DESCONTO) ---
# Verifica a faixa de valor da compra para definir o percentual de desconto:
# Compra menor que R$ 100.00: Sem desconto (0%)
if valor_compra < 100.00:
    percentual_desconto = 0.00

# Compra entre R$ 100.00 e R$ 199.99: 5% de desconto
elif valor_compra < 200.00:
    percentual_desconto = 0.05

# Compra entre R$ 200.00 e R$ 299.99: 10% de desconto
elif valor_compra < 300.00:
    percentual_desconto = 0.10

# Compra igual ou superior a R$ 300.00: 15% de desconto
else:
    percentual_desconto = 0.15

# --- CÁLCULOS MATEMÁTICOS ---
# Calcula o valor exato em Reais (R$) do desconto concedido
valor_desconto = valor_compra * percentual_desconto

# Calcula o valor final com a dedução do desconto aplicado
valor_final = valor_compra - valor_desconto

# --- EXIBIÇÃO DOS RESULTADOS (SAÍDA FORMATADA) ---
# Exibe a tabela de resumo final formatando os valores numéricos com duas casas decimais (.2f)
print("\n==================================")
print("       RESUMO DO DESCONTO         ")
print("==================================")
print(f"Valor original:  R$ {valor_compra:.2f}")
print(f"Desconto ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
print("----------------------------------")
print(f"Total a pagar:   R$ {valor_final:.2f}")
print("==================================")
