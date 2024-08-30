import random
import matplotlib.pyplot as plt

def equacao_reta(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    return a, b, c

def verificar_lado_ponto(a, b, c, x, y):
    resultado = a * x + b * y + c
    return resultado > 0

def verifica_se_esta_dentro_triangulo(xp, yp, xa, ya, xb, yb, xc, yc):
    a1, b1, c1 = equacao_reta(xa, ya, xb, yb)
    a2, b2, c2 = equacao_reta(xb, yb, xc, yc)
    a3, b3, c3 = equacao_reta(xc, yc, xa, ya)
    
    lado1 = verificar_lado_ponto(a1, b1, c1, xp, yp)
    lado2 = verificar_lado_ponto(a2, b2, c2, xp, yp)
    lado3 = verificar_lado_ponto(a3, b3, c3, xp, yp)
    
    return (lado1 == lado2 == lado3)

def simular_area_lago(numero_simulacoes, xa, ya, xb, yb, xc, yc):
    area_quadrado = 4 * 4  # 4 km x 4 km
    area_total = 0
    pontos_x = []
    pontos_y = []
    pontos_dentro_x = []
    pontos_dentro_y = []

    for _ in range(numero_simulacoes):
        pontos_dentro = 0
        pontos_totais = 10000  # Número de pontos para cada simulação

        for _ in range(pontos_totais):
            xp = random.uniform(0, 4)  # x em [0, 4]
            yp = random.uniform(0, 4)  # y em [0, 4]
            
            pontos_x.append(xp)
            pontos_y.append(yp)
            
            if verifica_se_esta_dentro_triangulo(xp, yp, xa, ya, xb, yb, xc, yc):
                pontos_dentro_x.append(xp)
                pontos_dentro_y.append(yp)
                pontos_dentro += 1
        
        proporcao_dentro = pontos_dentro / pontos_totais
        area_lago = proporcao_dentro * area_quadrado
        area_total += area_lago
        
    area_media = area_total / numero_simulacoes

    # Plotando os pontos
    plt.figure(figsize=(8, 8))
    plt.scatter(pontos_x, pontos_y, color='yellow', s=1, label='Pontos dentro do quadrado')
    plt.scatter(pontos_dentro_x, pontos_dentro_y, color='red', s=1, label='Pontos dentro do triângulo')
    
    # Adicionando o triângulo ao gráfico
    triangulo_x = [xa, xb, xc, xa]
    triangulo_y = [ya, yb, yc, ya]
    plt.plot(triangulo_x, triangulo_y, color='green', linestyle='-', linewidth=2, label='Triângulo')

    # Adicionando o quadrado ao gráfico
    quadrado_x = [0, 4, 4, 0, 0]
    quadrado_y = [0, 0, 4, 4, 0]
    plt.plot(quadrado_x, quadrado_y, color='black', linestyle='--', linewidth=2, label='Quadrado')

    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.xlabel('X (km)')
    plt.ylabel('Y (km)')
    plt.title('Simulação de Monte Carlo - Pontos Aleatórios e Triângulo')
    plt.legend()
    plt.grid(True)
    plt.show()

    return area_media

# Definindo as coordenadas do triângulo 
XA, YA = 1.0, 1.0
XB, YB = 3.0, 1.0
XC, YC = 2.0, 3.0

# Simulação de Monte Carlo
numero_simulacoes = 50
area_lago_estimativa = simular_area_lago(numero_simulacoes, XA, YA, XB, YB, XC, YC)

print(f"A estimativa da área do lago é: {area_lago_estimativa:.2f} km²")
