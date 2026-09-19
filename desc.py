# ==========================================================
# Programa: Sistema de Desconto Progressivo
# Descrição: Recebe o valor total de uma compra, calcula o
#            desconto progressivo aplicado e o valor final a pagar.
# ==========================================================

def calcular_desconto_progressivo():
    try:
        # Entrada de dados: solicita o valor total da compra ao usuário
        valor_compra = float(input("Digite o valor total da compra (R$): "))

        # Validação para evitar valores negativos
        if valor_compra < 0:
            print("Erro: O valor da compra não pode ser negativo.")
            return

        # Estrutura de decisão para aplicar as regras de desconto
        if valor_compra < 200.00:
            porcentagem = 5
            percentual_desconto = 0.05   # 5% para compras abaixo de R$ 200,00
        elif valor_compra < 300.00:
            porcentagem = 10
            percentual_desconto = 0.10   # 10% para compras entre R$ 200,00 e R$ 299,99
        else:
            porcentagem = 15
            percentual_desconto = 0.15   # 15% para compras a partir de R$ 300,00

        # Processamento de dados: cálculos do desconto e total a pagar
        valor_desconto = valor_compra * percentual_desconto
        valor_final = valor_compra - valor_desconto

        # Saída de dados: exibe o resumo completo com valores formatados
        print("\n--- RESUMO DA COMPRA ---")
        print(f"Valor original da compra : R$ {valor_compra:.2f}")
        print(f"Desconto aplicado        : {porcentagem}%")
        print(f"Valor do desconto        : R$ {valor_desconto:.2f}")
        print(f"Valor total a pagar      : R$ {valor_final:.2f}")

    except ValueError:
        print("Erro: Por favor, insira um número válido (ex: 150.50).")


# Ponto de entrada do programa
if __name__ == "__main__":
    calcular_desconto_progressivo()
