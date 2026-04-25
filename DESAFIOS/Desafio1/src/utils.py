def salvar_relatorio_txt(lista_funcionarios):
    if len(lista_funcionarios) == 0:
        print("Nenhum funcionario para salvar!")
        return

    with open("relatorio.txt", "w") as arquivo:
        total_liquido = 0
        
        for f in lista_funcionarios:
            linha = f"{f['nome']} ({f['tipo']}) - Bruto: R${f['bruto']:.2f} | Liquido: R${f['liquido']:.2f}\n"
            arquivo.write(linha)
            total_liquido += f['liquido']
        
        arquivo.write(f"\nTotal Empresa: R$ {total_liquido:.2f}")
        
    print("Relatorio salvo em 'relatorio.txt'!")