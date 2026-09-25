ano = int(input(" escreva a quantidade de dias no ano bissexto(366):"))
ano1 = input("escreva se esse ano é bissexto(SIM/NÃO:").upper()
if (ano /4)or not (ano /100) or (ano / 400) and ano1 == "SIM":
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")