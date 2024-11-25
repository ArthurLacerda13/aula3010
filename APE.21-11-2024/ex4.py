x = float(input("Qual foi a primeira nota? "))
y = float(input("Qual foi a primeira nota? "))
media = (x+y) /2
while x < 0 or x > 10 or y < 0 or y > 10:
    print("nota inválida")
    x = float(input("Qual foi a primeira nota? "))
    y = float(input("Qual foi a primeira nota? "))
    media = (x+y) /2    
print(media)
