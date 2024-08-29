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

lado_quadrado = float(input("Informe o lado do quadrado: "))
lado_triangulo = float(input("Informe o lado do triângulo: "))

XA = float(input("Informe o XA do triângulo: "))
YA = float(input("Informe o YA do triângulo: "))

XB = float(input("Informe o XB do triângulo: "))
YB = float(input("Informe o YB do triângulo: "))

XC = float(input("Informe o XC do triângulo: "))
YC = float(input("Informe o YC do triângulo: "))

xp = float(input("Informe o X do ponto: "))
yp = float(input("Informe o Y do ponto: "))

esta_dentro = verifica_se_esta_dentro_triangulo(xp, yp, XA, YA, XB, YB, XC, YC)
if esta_dentro:
    print(f"O ponto ({xp}, {yp}) está dentro do triângulo.")
else:
    print(f"O ponto ({xp}, {yp}) não está dentro do triângulo.")
