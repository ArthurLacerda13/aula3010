t = int(input("Quantas linhas a piramide devera ter? "))
if t > 0:
    for i in range(1, t+1):
        print(i*"*")
else:
    print(f"oh meu fi, num é possivi n, criar um triangulo com {t} linhas")
