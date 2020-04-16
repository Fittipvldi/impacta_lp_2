from escola import (adicionar_aluno, remover_aluno, pesquisar_aluno,
                    calcular_media, calcular_media_turma, melhores_alunos)

alunos = {'pedro': [10, 9.5, 9, 5, 7],
          'ana': [4, 7, 9.5, 10, 8],
          'jose': [10, 4.5, 5, 6, 8]}

listanotas = []

qtdalunos = int(input(" Insira a quantidade de alunos deseja incluir: "))
for i in range(qtdalunos):
    nome1 = input("Insira o nome do aluno: ")
    for i in range(5):
        nota = float(input("Insira a nota do aluno: "))
        listanotas.append(nota)
    retorna1 = adicionar_aluno(alunos, nome1, listanotas)
    listanotas = []
    print(retorna1)

nome2 = input("Insira o nome do aluno que deseja excluir: ")
retorna2 = remover_aluno(alunos, nome2)
print(retorna2)

nome3 = input("Insira o nome do aluno no qual deseja ver as notas: ")
retorna3 = pesquisar_aluno(alunos, nome3)
print(retorna3)

nome4 = input("Insira o nome do aluno no qual deseja ver a média das notas: ")
retorna4 = calcular_media(alunos, nome4)
print(f"A média do {nome4} é de {retorna4}")

retorna5 = calcular_media_turma(alunos)
print(f"A média da turma é de {retorna5}")

retorna6 = melhores_alunos(alunos)
print(f"O melhor aluno é: {retorna6}")
