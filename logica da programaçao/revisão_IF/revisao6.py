lado = int(input("escreva um valor:"))
lado2 = int(input("escreva um valor:"))
lado3 = int(input("escreva um valor:"))
if (lado+lado2>lado3) and (lado+lado3>lado2) and (lado2+lado3>lado):
    print("Triangulo valido")
else:
    print("nao é um triangulo")