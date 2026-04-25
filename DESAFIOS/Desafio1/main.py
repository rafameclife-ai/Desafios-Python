from src.regras_negocio import cadastrar_funcionario, exibir_relatorio, banco_funcionarios
from src.utils import salvar_relatorio_txt

def main():
    while True:
        print("\nSISTEMA DE FUNCIONARIOS")
        print("1. Cadastrar")
        print("2. Relatorio") 
        print("3. Salvar")
        print("4. Sair")
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            nome = input("Nome do funcionario: ")
            if nome == "":
                print("Nome nao pode estar vazio!")
                continue
                
            tipo = input("Tipo (estagiario/clt/freelancer): ").lower()
            
            bruto = 0
            v_hora = 0
            horas = 0
            
            if tipo == "freelancer":
                v_hora = float(input("Valor por hora: "))
                horas = float(input("Horas trabalhadas: "))
            elif tipo in ["clt", "estagiario"]:
                bruto = float(input("Salario bruto: "))
            else:
                print("Tipo invalido! Use: estagiario, clt ou freelancer")
                continue
                
            sucesso, mensagem, liquido = cadastrar_funcionario(nome, tipo, bruto, v_hora, horas)
            
            print(mensagem)
            if sucesso:
                print(f"Liquido: R$ {liquido:.2f}")

        elif opcao == "2":
            exibir_relatorio()

        elif opcao == "3":
            salvar_relatorio_txt(banco_funcionarios)

        elif opcao == "4":
            print("Ate logo!")
            break
        
        else: 
            print("Opcao invalida!")

if __name__ == "__main__":
    main()