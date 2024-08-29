import matplotlib.pyplot as plt

contagem_comparacoes = 0

def hanoi(n, o, d, a):
    global contagem_comparacoes
    if n == 1:
        contagem_comparacoes += 1
    else:
        hanoi(n-1, o, a, d)
        contagem_comparacoes += 1
        hanoi(n-1, a, d, o)

def calcular_comparacoes(n):
    global contagem_comparacoes
    contagem_comparacoes = 0
    hanoi(n, 'A', 'B', 'C')
    return contagem_comparacoes

valores_n = list(range(3, 21))
comparacoes = [calcular_comparacoes(n) for n in valores_n]

plt.figure(figsize=(10, 6))
plt.plot(valores_n, comparacoes, marker='o', linestyle='-', color='b')
plt.xlabel('Número de Discos (n)')
plt.ylabel('Número de Comparações')
plt.title('Número de Comparações no Problema das Torres de Hanoi')
plt.grid(True)
plt.show()
