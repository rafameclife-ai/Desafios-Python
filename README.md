# Desafios-Python
# Desafios de Python - Prof. Max

funcionarios = []

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
        
  if tipo == "freelancer":
            v_hora = float(input("Valor por hora: "))
            horas = float(input("Horas trabalhadas: "))
            bruto = v_hora * horas
            inss = 0
            irrf = bruto * 0.05
        elif tipo == "clt":
            bruto = float(input("Salario bruto: "))
            inss = bruto * 0.08
            if bruto > 2000:
                irrf = bruto * 0.10
            else:
                irrf = 0
        elif tipo == "estagiario":
            bruto = float(input("Salario bruto: "))
            inss = 0
            irrf = 0
        else:
            print("Tipo invalido! Use: estagiario, clt ou freelancer")
            continue

  liquido = bruto - inss - irrf
        
 funcionario = {
            "nome": nome,
            "tipo": tipo.title(),
            "bruto": bruto,
            "inss": inss,
            "irrf": irrf,
            "liquido": liquido
        }
        funcionarios.append(funcionario)
        print(f"{nome} cadastrado com sucesso!")
        print(f"Liquido: R$ {liquido:.2f}")


  elif opcao == "2":
        if len(funcionarios) == 0:
            print("Nenhum funcionario cadastrado!")
        else:
            total_liquido = 0
            print("\n=== RELATORIO ===")
            for f in funcionarios:
                print(f"{f['nome']} ({f['tipo']})")
                print(f"  Bruto: R$ {f['bruto']:.2f}")
                print(f"  INSS: R$ {f['inss']:.2f}")
                print(f"  IRRF: R$ {f['irrf']:.2f}")
                print(f"  Liquido: R$ {f['liquido']:.2f}\n")
                total_liquido = total_liquido + f['liquido']
            print(f"TOTAL DA EMPRESA: R$ {total_liquido:.2f}")

  elif opcao == "3":
        if len(funcionarios) == 0:
            print("Nenhum funcionario para salvar!")
        else:
            arquivo = open("relatorio.txt", "w")
            total_liquido = 0
            
  for f in funcionarios:
                linha = f"{f['nome']} ({f['tipo']}) - Bruto: R${f['bruto']:.2f} | Liquido: R${f['liquido']:.2f}\n"
                arquivo.write(linha)
                total_liquido = total_liquido + f['liquido']
            
  arquivo.write(f"Total Empresa: R$ {total_liquido:.2f}")
            arquivo.close()
            print("Relatorio salvo em 'relatorio.txt'!")

  elif opcao == "4":
        print("Ate logo!")
        break
    
    else:
        print("Opcao invalida!")
