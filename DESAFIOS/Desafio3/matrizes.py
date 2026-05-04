import random

matriz_aleatoria = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]

print("--- Matriz 3x3 Aleatória ---")
for linha in matriz_aleatoria:
    print(linha)

vendas_loja_a = [[10, 20, 30],
                 [15, 25, 35]]

vendas_loja_b = [[5, 10, 15],
                 [10, 5, 10]]

soma_vendas = [
    [a + b for a, b in zip(linha_a, linha_b)]
    for linha_a, linha_b in zip(vendas_loja_a, vendas_loja_b)
]

print("\n--- Soma das Matrizes (Vendas Consolidadas) ---")
for linha in soma_vendas:
    print(linha)

total_geral = sum(sum(linha) for linha in soma_vendas)
print(f"Total de vendas: {total_geral}")

notas_estudantes = [
    [8.5, 7.0, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 10.0]
]

medias_finais = [round(sum(aluno) / len(aluno), 2) for aluno in notas_estudantes]

print("\n--- Médias dos Alunos ---")
print(medias_finais)

matriz_sistema = [
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
]

m = matriz_sistema
determinante = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

print(f"\n--- Determinante: {determinante} ---")

if determinante != 0:
    print("Status: Sistema resolvível (matriz invertível)")
else:
    print("Status: Sistema NÃO resolvível (matriz singular)")

tabela_estoque = [
    [10, 20],
    [30, 40],
    [50, 60]
]

tabela_precos = [
    [2, 3, 4]
]

estoque_transposto = [list(linha) for linha in zip(*tabela_estoque)]

valor_total = [
    [sum(a * b for a, b in zip(linha_preco, coluna_estoque)) for coluna_estoque in zip(*estoque_transposto)]
    for linha_preco in tabela_precos
]

print("\n--- Estoque Transposto ---")
for linha in estoque_transposto:
    print(linha)

print("\n--- Valor Total Calculado ---")
for linha in valor_total:
    print(linha)
