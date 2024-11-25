print('''1.Álcool
2.Gasolina
3.Diesel
4.FIm
''')
alcool = gasolina = diesel = 0
combustivel = int(input("Digite o número referente à seu combustível de preferência: "))
while combustivel != 4:
        if combustivel == 1:
            alcool = alcool+1
        elif combustivel == 2:
            gasolina = gasolina+1
        elif combustivel == 3:
            diesel = diesel+1
        combustivel = int(input("Digite o número referente à seu combustível de preferência: "))
            
print("seu programa foi encerrado")
print(f'''
Álcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}
''')
