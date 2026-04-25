from src.produtos import cadastrar_produto
from src.operacoes import realizar_venda
from src.relatorio import gerar_relatorio_tela, salvar_relatorio_arquivo
from src.teste_vendas import rodar_testes_simples

def main():
    produtos = []
    vendas = []

    while True:
        print("\n=== SISTEMA ===")
        print("1. Cadastrar produto")
        print("2. Realizar venda")
        print("3. Gerar relatório")
        print("4. Salvar relatório")
        print("5. Rodar teste")
        print("6. Sair")
        
        opcao = input("Escolha: ").strip()

        if opcao == '1':
            cadastrar_produto(produtos)
        elif opcao == '2':
            realizar_venda(produtos, vendas)
        elif opcao == '3':
            gerar_relatorio_tela(vendas)
        elif opcao == '4':
            salvar_relatorio_arquivo(vendas)
        elif opcao == '5':
            rodar_testes_simples()
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()