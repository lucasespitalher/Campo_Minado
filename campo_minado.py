from random import randint


class CampoMinado():

    def __init__(self, linhas:int=10, colunas:int=10, bombas:int=10):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.campo_minado = dict([((linha, coluna), None) for linha in range(self.linhas) for coluna in range(self.colunas)])
        self.plantar_bombas()
        self.plantar_numeros()
        self.coordenada = set()

        self.tabuleiro_visivel = [["|  " for linha in range(self.linhas)] for coluna in range(self.colunas)] #

    def plantar_bombas(self):
        contador = 0
        while contador < self.bombas:
            lin = randint(0, self.linhas-1)
            col = randint(0, self.colunas-1)
            if self.campo_minado[(lin, col)] == None:
                self.campo_minado[(lin, col)] = -1
                contador += 1

    def plantar_numeros(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if self.campo_minado[(linha, coluna)] != -1:
                    contador = 0
                    for lin in range(max(0 , linha-1), min(self.linhas-1, linha+1)+1):
                        for col in range(max(0 , coluna-1), min(self.colunas-1, coluna+1)+1):
                            if lin == linha and col == coluna:
                                continue

                            if self.campo_minado[(lin, col)] == -1:
                                contador += 1

                    self.campo_minado[(linha, coluna)] = contador

    def revelar_coordenadas(self, linha, coluna):
        self.coordenada.add((linha, coluna))

        if self.campo_minado[(linha, coluna)] == -1:
            return False

        elif self.campo_minado[(linha, coluna)] > 0:
            return True

        for lin in range(max(0, linha-1), min(self.linhas-1, linha+1)+1):
            for col in range(max(0, coluna-1), min(self.colunas-1, coluna+1)+1):
                if (lin, col) in self.coordenada:
                    continue

                self.revelar_coordenadas(lin, col)

        return True

    def __str__(self): #
        for tupla in self.coordenada:
            if self.campo_minado[(tupla)] == -1:
                self.tabuleiro_visivel[tupla[0]][tupla[1]] = f"|{self.campo_minado[(tupla)]}"
            else: self.tabuleiro_visivel[tupla[0]][tupla[1]] = f"| {self.campo_minado[(tupla)]}"

        lista = []
        for item in self.tabuleiro_visivel:
            lista.append(("").join(item))

        cabecalho = []
        for num in range(self.linhas):
            cabecalho.append(f" {num} ")

        print("\n" + "  ", ("").join(cabecalho))

        for i, item in enumerate(lista):
            print(i, item + '|')

        return ''


def main():
    campo_minado = CampoMinado()
    check = True 

    while len(campo_minado.coordenada) < (campo_minado.linhas * campo_minado.colunas - campo_minado.bombas):
        
        print(campo_minado)

        linha = input("Linha: ")
        coluna = input("Coluna: ")

        if linha.isnumeric() == False or coluna.isnumeric() == False:
            print("Digite Apenas Números.")
            continue

        linha, coluna = int(linha), int(coluna)

        if linha < 0 or linha >= campo_minado.linhas or coluna < 0 or coluna >= campo_minado.colunas:
            print("Localização Inválida.")
            continue

        check = campo_minado.revelar_coordenadas(linha, coluna)
        if check == False:
            break

    if check:
        print(">>>>> VOCÊ VENCEU!!! <<<<<\n")

    else:
        campo_minado.coordenada = [(lin, col) for lin in range(campo_minado.linhas) for col in range(campo_minado.colunas)]
        print(campo_minado)
        print(">>>>> GAME OVER <<<<<\n")

if __name__ == '__main__':
    main()