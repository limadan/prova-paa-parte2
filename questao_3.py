import math
import random

def aleatorio(a, b):
    n = b - a
    c = int(math.log2(n)) + 1
    while True:
        r = ''.join(str(random.randint(0, 1)) for _ in range(c))
        num = int(r, 2)
        if num <= n:
            result = a + num
            #print(f'Número gerado: {result}')
            return result

ini_interv = int(input("Digite ini_interv: "))
fim_interv = int(input("Digite fim_interv: "))
linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))


if ini_interv >= fim_interv:
    print("O valor de 'a' deve ser menor que 'b'.")
else:
    matriz = []

    for i in range(0, linhas, 1):
        linha = []
        for j in range(0, colunas, 1):
            linha.append(aleatorio(ini_interv, fim_interv))
        matriz.append(linha)

    print("Resultado:")
    for i in range (0, linhas, 1):
        print(matriz[i])
