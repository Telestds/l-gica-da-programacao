mensal = int(input("escreva sua renda mensal:"))
parcela = int(input("escreva o valor da parcela:"))
if (mensal>= 3000) and (parcela<= (mensal*0.3)):
    print("aprovado")
else:
    print("emprestimo negado")