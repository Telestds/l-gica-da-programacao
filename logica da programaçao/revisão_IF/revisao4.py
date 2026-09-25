sistema = input("digite o status do sistema(MANUTENÇÃO/ATIVO)").upper()
if  not sistema == "MANUTENÇÃO":
    print("acesso liberado")
else:
    print("sistema em manutenção, tente mais tarde")