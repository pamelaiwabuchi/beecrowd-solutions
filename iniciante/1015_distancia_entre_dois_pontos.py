import math
entrada = input().split()

x1 = float(entrada[0])
y1 = float(entrada[1])

entrada2 = input().split()


x2 = float(entrada2[0])
y2 = float(entrada2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")