school= input("possuí nivel superior completo(SIM/NÃO):").upper()
experiências = int(input("possuí quantos anos de experiências:"))
if (school == "SIM" and experiências) >= 2 or (experiências> 5 and school == "NÃO"):
    print("convocado para entrevista")
else:
    print("perfil não atende aos requesitos")
