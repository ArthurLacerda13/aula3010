primo = 0
n = int(input("digite um número inteiro: "))
for i in range(2, n):
    if n%i == 0:
        primo = primo + 1

if primo != 0:
    print("Não é primo")
else:
    print("É primo")
    
