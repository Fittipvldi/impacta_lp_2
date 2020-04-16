# Henrique Fittipaldi              RA: 1901257
# Guilherme Trindade               RA:1901907
# Paulo Henrique Gomes de Oliveira RA:1902349


def calculo(lista):
    # Professor, eu não tinha ideia de como economizar linha nesse trecho :(
    if lista[3] == "DESENVOLVEDOR" or lista[3] == "ANALISTA" or lista[3] == "GERENTE":
        novosalario = 0
        if lista[3] == "DESENVOLVEDOR":
            if lista[2] >= 3000:
                novosalario = lista[2] - lista[2] * 0.20
                return novosalario
            else:
                novosalario = lista[2] - lista[2] * 0.10
                return novosalario

        if lista[3] == "ANALISTA":
            if lista[2] >= 2000:
                novosalario = lista[2] - lista[2] * 0.25
                return novosalario
            else:
                novosalario = lista[2] - lista[2] * 0.15
                return novosalario

        if lista[3] == "GERENTE":
            if lista[2] >= 5000:
                novosalario = lista[2] - lista[2] * 0.30
                return novosalario
            else:
                novosalario = lista[2] - lista[2] * 0.20
                return novosalario
    else:
        raise TypeError
