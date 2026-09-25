idade = int(input("escreva sua idade:"))
cadastro = input("você possuí cadastro(SIM/NÃO):").upper()
if idade< 12 or idade >=65 or cadastro =="SIM":
    print("entrada gratuita")
else:
    print("entrada paga")
