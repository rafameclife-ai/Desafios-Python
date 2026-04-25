from src.produtos import listar_produtos

def realizar_venda(lista_produtos, lista_vendas):
    print("\n--- Realizar Venda ---")
    cliente = input("Nome do cliente: ").strip()
    
    if not cliente:
        print("Erro: Nome do cliente vazio.")
        return

    if not listar_produtos(lista_produtos):
        return

    try:
        escolha = int(input("\nSelecione o produto pelo número: ")) - 1
        
        if escolha < 0 or escolha >= len(lista_produtos):
            print("Erro: Produto inexistente.")
            return

        produto = lista_produtos[escolha]
        quantidade = int(input(f"Quantidade de {produto['nome']}: "))
        
        if quantidade <= 0:
            print("Erro: Quantidade inválida.")
            return

        if quantidade > produto["estoque"]:
            print("Erro: Estoque insuficiente.")
            return

        valor_bruto = produto["preco"] * quantidade
        desconto = valor_bruto * 0.05 if quantidade > 10 else 0.0
        valor_final = valor_bruto - desconto

        produto["estoque"] -= quantidade

        lista_vendas.append({
            "cliente": cliente,
            "produto": produto["nome"],
            "quantidade": quantidade,
            "valor_bruto": valor_bruto,
            "desconto": desconto,
            "valor_final": valor_final
        })
        
        print(f"Venda realizada! Valor final: R$ {valor_final:.2f}")

    except ValueError:
        print("Erro: Digite apenas números.")