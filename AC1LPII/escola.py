# Atividade Contínua 01
# Aluno 01: Guilherme Valverde Trindade     RA = 1901907
# Aluno 02: Henrique Fittipaldi     RA = 1901257


def adicionar_aluno(alunos, nome, notas):
    '''
    Essa função acrescenta os dados de um novo aluno no dicionário
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
        notas: lista com as notas de um aluno (valor)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave já exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''

    if nome in alunos:
        return alunos
    else:
        alunos[nome] = notas
        return alunos


def remover_aluno(alunos, nome):
    '''
    Essa função exclui os dados de um aluno do dicionário.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''

    if nome in alunos:
        alunos.pop(nome)
        return alunos
    else:
        return alunos


def pesquisar_aluno(alunos, nome):
    '''
    Essa função deve retornar a lista com as notas de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar uma lista com as notas do aluno
    Observação:
        Caso a chave não exista, deve retornar uma lista vazia
    '''
    vazia = []
    if nome in alunos:
        return alunos[nome]
    else:
        return vazia


def calcular_media(alunos, nome):
    '''
    Essa função retorna a média de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar a média do aluno
    Observação:
        Caso a chave não exista, deve retornar zero
    '''
    media = 0
    if nome in alunos:
        media = sum(alunos[nome])/len(alunos[nome])
        return media
    else:
        return 0


def calcular_media_turma(alunos):
    '''
    Essa função retorna a média geral da turma
    (soma de todas as notas dividida pela quantidade de todas as notas)
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar a média geral da turma
    '''

    notas = []
    for nome in alunos:
        notas = notas + alunos[nome]
    return sum(notas) / len(notas)


def melhores_alunos(alunos):
    '''
    Essa função retorna o nome do aluno com a maior média
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar o nome do aluno que obteve a maior média
    Observação:
        Caso haja mais que um aluno com a maior média,
        pode retorna qualquer um deles
    '''
    media = 0
    for nome in alunos:
        if sum(alunos[nome])/len(alunos[nome]) > media:
            media = sum(alunos[nome])/len(alunos[nome])
            best = nome
    return best
