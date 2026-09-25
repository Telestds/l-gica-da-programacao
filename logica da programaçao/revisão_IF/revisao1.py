idade = int(input("escreva sua idade:"))
carteira = input(" tem carteira de motorista(SIM/NÃO):").upper()
if idade>= 18 and carteira =="SIM":
    print("pode dirigir")
else:
    print("nao pode dirigir")