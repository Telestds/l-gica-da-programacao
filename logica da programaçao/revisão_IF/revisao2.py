# idade = int(input("escreva sua idade:"))
estudante = input("escreva se voce é estudante(SIM/NÃO):").upper()
if (int(input("escreva sua idade:"))>= 60) and estudante == "SIM":
    print("tem direito ao desconto")
else:
    print("pagamento integral")