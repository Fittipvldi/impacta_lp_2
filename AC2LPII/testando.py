# Henrique Fittipaldi              RA: 1901257
# Guilherme Trindade               RA:1901907
# Paulo Henrique Gomes de Oliveira RA:1902349

from salariocalc import calculo

lista = ["Marcílio dos Santos", "marcilio@email.com", 5000.00, "PROFESSOR"]
lista1 = ["Marcílio dos Santos", "marcilio@email.com", 5000.00,
          "DESENVOLVEDOR"]
lista2 = ["Marcílio dos Santos", "marcilio@email.com", 2000.00,
          "DESENVOLVEDOR"]
lista3 = ["Marcílio dos Santos", "marcilio@email.com", 3000.00, "ANALISTA"]
lista4 = ["Marcílio dos Santos", "marcilio@email.com", 1000.00, "ANALISTA"]
lista5 = ["Marcílio dos Santos", "marcilio@email.com", 6000.00, "GERENTE"]
lista6 = ["Marcílio dos Santos", "marcilio@email.com", 4000.00, "GERENTE"]

try:
    retorno = calculo(lista)
    print("Correto")
except TypeError:
    print("O cargo não existe")

try:
    retorno = calculo(lista1)
    assert retorno == 4000
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 4000)

try:
    retorno = calculo(lista2)
    assert retorno == 1800
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 1800)

try:
    retorno = calculo(lista3)
    assert retorno == 2250
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 2250)

try:
    retorno = calculo(lista4)
    assert retorno == 850
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 850)

try:
    retorno = calculo(lista5)
    assert retorno == 4200
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 4200)

try:
    retorno = calculo(lista6)
    assert retorno == 3200
    print("correto")
except AssertionError:
    print("ERRO")
    print("Retorno: ", retorno)
    print("Esperado: ", 3200)
