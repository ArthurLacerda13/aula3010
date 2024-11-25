x = int(input("informe a coordenada x: "))
y = int(input("informe a coordenada y: "))
while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("primeiro quadrante")
    elif x < 0 and y > 0:
        print("segundo quadrante")
    elif x < 0 and y < 0:
        print("terceiro quadrante")
    elif x > 0 and y < 0:
        print("quarto quadrante")
    x = int(input("informe a coordenada x: "))
    y = int(input("informe a coordenada y: "))
print("programa encerrado")
