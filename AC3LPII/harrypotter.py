# Henrique Garcia Fittipaldi RA:1901257
# Guilherme Valverde Trindade RA: 1901257
# Paulo Henrique Gomes de Oliveira RA: 1902349


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None

    def set_diretor(self, professor):
        self.diretor = professor

    def set_monitor(self, aluno):
        self.monitor = aluno


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa
        self.alunos = []

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, triunfo):
        self.__triunfos += triunfo

    def incluir_mau_feito(self, mau_feito):
        self.__mau_feitos += mau_feito

    def get_triunfo(self):
        return self.__triunfos

    def get_mau_feito(self):
        return self.__mau_feitos


class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, pontos):
        if casa == self.casa1:
            self.__pontos_casa1 += pontos
        else:
            self.__pontos_casa2 += pontos

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2

# PROGRAMA PRINCIPAL


# Escola
hogwarts = Escola("Escola de Magia e Bruxaria de Hogwarts")

# Casas
grifinoria = Casa("Grifinória", "Leão")
sonserina = Casa("Sonserina", "Serpente")
corvinal = Casa("Corvinal", "Corvo")
lufalufa = Casa("Lufa-Lufa", "Texugo")

# Disciplinas
herbologia = Disciplina("Herbologia", "Ervas e Fungos Mágicos, Árvores que se Alimentam de Carne")
transfiguracao = Disciplina("Transfiguracao", "Transfiguração Entre Espécies, Transfiguração Humana")
pocoes = Disciplina("Poções", "Poções Simples, Poções Avançadas")
defesa = Disciplina("Defesa contra as artes das trevas", "Maldição Cruciatus, Dementadores, Feitiços não-verbais")

# Professores
minerva = Professor("Minerva McGonagall", "19351004")
filio = Professor("Fílio Flitwick", "19301017")
pomona = Professor("Pomona Sprout", "19410515")
severo = Professor("Severo Snape", "19600109" )

# Alunos
draco = Aluno("Draco Malfoy", "19800605", "puro-sangue")
ernesto = Aluno("Ernesto Macmillan", "19800901", "puro-sangue")
hermione = Aluno("Hermione Granger", "19790919", "trouxa")
harry = Aluno("Harry Potter", "19800731", "mestiço")
luna = Aluno("Luna Lovegood", "19810213", "puro-sangue")

# inclui as casas na escola
hogwarts.incluir_casa(grifinoria)
hogwarts.incluir_casa(sonserina)
hogwarts.incluir_casa(corvinal)
hogwarts.incluir_casa(lufalufa)

# definição dos diretores das casas
grifinoria.set_diretor(minerva)
sonserina.set_diretor(severo)
corvinal.set_diretor(filio)
lufalufa.set_diretor(pomona)

# definicao dos monitores das casas
grifinoria.set_monitor(hermione)
sonserina.set_monitor(draco)
corvinal.set_monitor(ernesto)
lufalufa.set_monitor(luna)

# definição das casas dos alunos
draco.set_casa(sonserina)
ernesto.set_casa(corvinal)
hermione.set_casa(grifinoria)
harry.set_casa(grifinoria)
luna.set_casa(lufalufa)

# definicao dos professores das disciplinas
severo.incluir_disciplina(defesa)
severo.incluir_disciplina(transfiguracao)
minerva.incluir_disciplina(herbologia)
filio.incluir_disciplina(transfiguracao)
pomona.incluir_disciplina(pocoes)

# Definição dos alunos que cursam as disciplinas
herbologia.incluir_aluno(harry)
herbologia.incluir_aluno(hermione)
transfiguracao.incluir_aluno(draco)
transfiguracao.incluir_aluno(hermione)
pocoes.incluir_aluno(ernesto)
defesa.incluir_aluno(harry)
defesa.incluir_aluno(draco)
defesa.incluir_aluno(ernesto)
defesa.incluir_aluno(hermione)
defesa.incluir_aluno(luna)

# triunfos e mau_feitos
harry.incluir_triunfo(3)
harry.incluir_mau_feito(1)
draco.incluir_mau_feito(2)
draco.incluir_triunfo(1)
hermione.incluir_triunfo(4)
harry.incluir_triunfo(2)

# Cria o torneio de Quadribol
torneio = Torneio(sonserina, grifinoria)
torneio.marcar_ponto(sonserina, 2)
torneio.marcar_ponto(grifinoria, 1)
torneio.marcar_ponto(grifinoria, 3)
torneio.marcar_ponto(sonserina, 1)

# IMPRESSAO DE VALORES PARA TESTE       # VALORES A SER IMPRESSOS
print(hogwarts.nome)                    # Escola de Magia e Bruxaria de Hogwarts
print(len(hogwarts.casas))              # 4
print(sonserina.nome)                   # Sonserina
print(sonserina.animal)                 # Serpente
print(grifinoria.diretor.nome)          # Minerva McGonagall
print(grifinoria.monitor.nome)          # Hermione Granger
print(minerva.nome)                     # Minerva McGonagall
print(severo.nascimento)                # 19600109
print(severo.disciplinas[1].nome)       # Transfiguracao
print(defesa.nome)                      # Defesa contra as artes das trevas
print(herbologia.ementa)                # Ervas e Fungos Mágicos, Árvores que se Alimentam de Carne
print(len(defesa.alunos))               # 5
print(defesa.alunos[0].nome)            # Harry Potter
print(luna.nome)                        # Luna Lovegood
print(luna.nascimento)                  # 19810213
print(draco.tipo)                       # puro-sangue
print(draco.casa.nome)                  # Sonserina
print(hermione.get_triunfo())           # 4
print(draco.get_mau_feito())            # 2
print(torneio.casa1.nome)               # Sonserina
print(torneio.casa2.nome)               # Grifinória
print(torneio.get_pontos_casa1())       # 3
print(torneio.get_pontos_casa2())       # 4
