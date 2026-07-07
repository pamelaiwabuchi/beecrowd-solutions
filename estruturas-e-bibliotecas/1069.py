#Diamantes e Areia

import sys

def main():
    #o readline vai literalmente ler cada linha, que deixa de existir no fluxo de leitura. No exemplo, a primeira linha de teste é 2.
    #isso significa que ao continuar a leitura, o 2, que já foi lido, é ignorado e ele segue lendo as próximas linhas.
    try:
        n = int(sys.stdin.readline())
    except (IOError, ValueError):
        return
    
    for _ in range(n): #usar _ ao inves de i indica que nao é necessária a criação de uma variável. O valor nao será usado.
        linha = sys.stdin.readline().strip()
        if not linha:
            continue

        diamantes = 0
        menores_acumulados = 0
            
        for caractere in linha:
            if caractere == '<':
                menores_acumulados += 1
            elif caractere == '>':
                if menores_acumulados > 0:
                    menores_acumulados -= 1
                    diamantes +=1
        
        print(diamantes)
                    
if __name__ == '__main__':
    main()