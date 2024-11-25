qnotas = 0
soma = 0
while True:
    idade = int(input("Qual a idade do indivíduo?"))
    if idade >= 0:
        qnotas += 1
        soma += idade
    else:
        break
print(soma/qnotas)