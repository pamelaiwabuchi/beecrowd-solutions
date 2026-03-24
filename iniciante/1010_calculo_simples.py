linha1 = input().split()
qt1 = int(linha1[1])
val1 = float(linha1[2])

linha2 = input().split()
qt2 = int(linha2[1])
val2 = float(linha2[2])

total = (qt1 * val1) + (qt2 * val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")