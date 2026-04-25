def cadastrar_produto(lista_produtos):
    print("\n--- Cadastrar Produto ---")
    nome = input("Nome do produto: ").strip()
    
    if not nome:
        print("Erro: Nome vazio.")
        return

    for p in lista_produtos:
        if p["nome"].lower() == nome.lower():
            print("Erro: Produto já cadastrado.")
            return

    try:
        preco = float(input("Preço (R$): "))
        if preco <= 0:
            print("Erro: Preço inválido.")
            return

        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Erro: Estoque inválido.")
            return

        lista_produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print("Produto cadastrado com sucesso.")
    except ValueError:
        print("Erro: Digite números válidos.")

def listar_produtos(lista_produtos):
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
        return False

    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(lista_produtos):
        print(f"{i + 1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")
    return True