# Programa de Pesquisa de Satisfação - TudoWeb

def pesquisa_satisfacao():
    # Defina como 10 para o teste de validação ou 50 para a pesquisa completa
    TOTAL_ENTREVISTADOS = 10  
    
    excelente = 0
    bom = 0
    ruim = 0

    print("=" * 50)
    print("      PESQUISA DE SATISFAÇÃO - TUDOWEB")
    print("=" * 50)

    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        nome = input("Digite seu nome: ").strip()
        idade = input("Digite sua idade: ").strip()
        
        # Estrutura para validação da opção digitada
        while True:
            print("\nQual a sua opinião sobre o atendimento prestado?")
            print("1 - EXCELENTE")
            print("2 - BOM")
            print("3 - RUIM")
            
            opcao = input("Digite o número da sua resposta (1, 2 ou 3): ").strip()
            
            # Estrutura de decisão para contabilizar a resposta
            if opcao == "1":
                excelente += 1
                break
            elif opcao == "2":
                bom += 1
                break
            elif opcao == "3":
                ruim += 1
                break
            else:
                print("\n[ERRO] Opção inválida! Digite apenas 1, 2 ou 3.")

    # Exibição dos resultados
    print("\n" + "=" * 50)
    print("           RESULTADO DA PESQUISA")
    print("=" * 50)
    print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {ruim}")
    print(f"   (Quantidade de respostas 'BOM': {bom})")
    print(f"   Total de participantes: {TOTAL_ENTREVISTADOS}")
    print("=" * 50)

if __name__ == "__main__":
    pesquisa_satisfacao()
