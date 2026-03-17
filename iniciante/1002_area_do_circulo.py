import sys

def main():
    entrada = sys.stdin.read().split()

    if not entrada:
        return

    raio = float(entrada[0])

    n = 3.14159
    area = n * (raio ** 2)

    sys.stdout.write(f"A={area:.4f}\n")

if __name__ == "__main__":
    main()