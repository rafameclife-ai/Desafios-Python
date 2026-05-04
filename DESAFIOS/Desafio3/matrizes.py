import random
import numpy as np

matriz = []
for _ in range(3):
    linha = []
    for _ in range(3):
        linha.append(random.randint(1, 100))
    matriz.append(linha)

print("Matriz 3x3 Aleatória:")
for linha in matriz:
    print(linha)

vendas1 = [[10, 20, 30], [15, 25, 35]]
vendas2 = [[5, 10, 15], [10, 5, 10]]
soma_vendas = []
total_vendas = 0

for i in range(len(vendas1)):
    linha = []
    for j in range(len(vendas1[0])):
        soma = vendas1[i][j] + vendas2[i][j]
        linha.append(soma)
        total_vendas += soma
    soma_vendas.append(linha)

print("\nSoma das Matrizes de Vendas:")
for linha in soma_vendas:
    print(linha)
print(f"Total de Vendas: {total_vendas}")

dados_alunos = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.0, 7.5],
    [9.5, 8.5, 10.0]
])

print("\nMédias dos Alunos por Linha:")
print(np.round(np.mean(dados_alunos, axis=1), 2))

sistema = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

det = round(np.linalg.det(sistema), 4)
print(f"\nDeterminante do Sistema: {det}")

if det != 0:
    print("O sistema é resolvível.")
else:
    print("O sistema NÃO é resolvível.")

estoque = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
precos = np.array([[5, 10, 15]])

print("\nTotais (Preços x Estoque Transposto):")
print(precos @ estoque.T)
