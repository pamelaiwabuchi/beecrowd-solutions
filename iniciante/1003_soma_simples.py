import sys

def soma():
    entrada = sys.stdin.read().split()

    if len(entrada) < 2:
        return
    A = int(entrada[0])
    B = int(entrada[1])
    soma = A + B

    sys.stdout.write(f"SOMA = {soma}\n")

if __name__ == "__main__":
    soma()