import sys

valor_entrada = float(sys.stdin.read())
centavos = int(valor_entrada * 100 + 0.5)

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

sys.stdout.write('NOTAS:\n')
for nota in notas:
    quantidade = centavos // nota
    centavos %= nota
    sys.stdout.write(f"{quantidade} nota(s) de R$ {nota/100:.2f}\n")

sys.stdout.write("MOEDAS:\n")
for moeda in moedas:
    quantidade = centavos // moeda
    centavos %= moeda
    sys.stdout.write(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}\n")


