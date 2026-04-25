def rodar_testes_simples():
    print("\n--- Rodando Testes ---")
    preco = 100.0
    quantidade = 15
    valor_bruto = preco * quantidade
    desconto = valor_bruto * 0.05 if quantidade > 10 else 0.0
    valor_final = valor_bruto - desconto
    
    if valor_final == 1425.0:
        print("Teste de desconto: OK")
    else:
        print("Teste de desconto: FALHOU")