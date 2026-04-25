def compilar_relatorio(lista_vendas):
    if not lista_vendas:
        return "Nenhuma venda realizada.\n"

    linhas = ["\n=== Relatório de Vendas ===", "--- Últimas Vendas (Máx 5) ---"]
    total = 0.0

    ultimas_vendas = lista_vendas[-5:]
    ultimas_vendas.reverse()

    for v in ultimas_vendas:
        linhas.append(f"Cliente: {v['cliente']}")
        linhas.append(f"Produto: {v['produto']}")
        linhas.append(f"Quantidade: {v['quantidade']}")
        linhas.append(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        linhas.append(f"Desconto: R$ {v['desconto']:.2f}")
        linhas.append(f"Valor Final: R$ {v['valor_final']:.2f}\n")

    for v in lista_vendas:
        total += v['valor_final']

    linhas.append(f"Total arrecadado: R$ {total:.2f}")
    return "\n".join(linhas)

def gerar_relatorio_tela(lista_vendas):
    print(compilar_relatorio(lista_vendas))

def salvar_relatorio_arquivo(lista_vendas):
    if not lista_vendas:
        print("Não há vendas para salvar.")
        return

    texto = compilar_relatorio(lista_vendas)
    caminho = input("Caminho do arquivo (Enter para 'relatorio_vendas.txt'): ").strip()
    
    if not caminho:
        caminho = "relatorio_vendas.txt"

    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(texto)
        print("Relatório salvo.")
    except Exception:
        print("Erro ao salvar o arquivo.")