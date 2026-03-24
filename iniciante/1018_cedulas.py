entrada = int(input())
dinheiro = [100,50,20,10,5,2,1]
notas = []
qtd = 0

print(entrada)

for i in dinheiro:
    qtd = entrada // i
    entrada = entrada % i
    notas.append(qtd)
    print(f'{qtd} nota(s) de R$ {i},00')