banco_funcionarios = []

def calcular_impostos(tipo, bruto=0, v_hora=0, horas=0):
    if tipo == "freelancer":
        bruto = v_hora * horas
        inss = 0
        irrf = bruto * 0.05
    elif tipo == "clt":
        inss = bruto * 0.08
        if bruto > 2000:
            irrf = bruto * 0.10
        else:
            irrf = 0
    elif tipo == "estagiario":
        inss = 0
        irrf = 0
    else:
        return None
    
    liquido = bruto - inss - irrf
    return bruto, inss, irrf, liquido

def cadastrar_funcionario(nome, tipo, bruto=0, v_hora=0, horas=0):
    resultado = calcular_impostos(tipo, bruto, v_hora, horas)
    
    if not resultado:
        return False, "Tipo invalido! Use: estagiario, clt ou freelancer", 0
        
    bruto_calc, inss, irrf, liquido = resultado
    
    funcionario = {
        "nome": nome,
        "tipo": tipo.title(),
        "bruto": bruto_calc,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido
    }
    
    banco_funcionarios.append(funcionario)
    return True, f"{nome} cadastrado com sucesso!", liquido

def exibir_relatorio():
    if len(banco_funcionarios) == 0:
        print("Nenhum funcionario cadastrado!")
        return

    total_liquido = 0
    print("\n=== RELATORIO ===")
    for f in banco_funcionarios:
        print(f"{f['nome']} ({f['tipo']})")
        print(f"  Bruto: R$ {f['bruto']:.2f}")
        print(f"  INSS: R$ {f['inss']:.2f}")
        print(f"  IRRF: R$ {f['irrf']:.2f}")
        print(f"  Liquido: R$ {f['liquido']:.2f}\n")
        total_liquido += f['liquido']
        
    print(f"TOTAL DA EMPRESA: R$ {total_liquido:.2f}")