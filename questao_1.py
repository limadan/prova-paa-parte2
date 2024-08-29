lado_quadrado = float(input("Informe o lado do quadrado: "))
lado_triangulo = float(input("Informe o lado do triângulo: "))

XA = float(input("Informe o XA do triângulo: "))
YA = float(input("Informe o YA do triângulo: "))

XB = float(input("Informe o XB do triângulo: "))
YB = float(input("Informe o YB do triângulo: "))

XC = float(input("Informe o XC do triângulo: "))
YC = float(input("Informe o YC do triângulo: "))

def vefifica_se_esta_dentro_triangulo(x_entrada, y_entrada):
    return (((YC-YA)/(XC-YA))*(x_entrada-XA) < y_entrada and
            ((YB-YA)/(BC-YA))*(x_entrada-XA) < y_entrada and
            ((YB-YC)/(XB-YC))*(x_entrada-XB) > y_entrada)

print(vefifica_se_esta_dentro_triangulo(2,1))