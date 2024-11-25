q = 0
n = int(input("digite um numero inteiro "))
for i in range(1, n+1):
    q = i * i
    if q <= n+1:
        resultado = q
print(resultado)
