# Sophia Louise Rodrigues da Luz  RA: 1801130
# Henrique Garcia Fittipaldi  RA: 1901257
# Guilherme Valverde Trindade  RA: 1901257
# Paulo Henrique Gomes de Oliveira  RA: 1902349

from abc import ABC, abstractmethod


class Cinema:
    def __init__(self, nome_cinema):
        self.nome_cinema = nome_cinema
        self.salas = []

    def incluir_salas(self, sala):
        self.salas.append(sala)


class Sala:
    def __init__(self, nome_cinema, nome_sala, capacidade):
        self.nome_sala = nome_sala
        self.capaciade = capacidade
        self.funcionarios = []
        self.filme = None
        self.horario = []

    def incluir_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)

    def passar_filme(self, filme):
        self.filme = filme

    def horario_exibicao(self, horario):

        for i in self.horario:
            if horario == i:
                print("Sala em uso.")
            else:
                pass

        if horario == "16:00" or horario == "17:00" or horario == "18:00" or horario == "19:30" or horario == "20:00" or horario == "22:00" or horario == "23:00":
            self.horario.append(horario)
        else:
            print("Horário Inválido")


class Filme:
    def __init__(self, nome_filme, nome_filme_original, diretor, ano_lancamento, tipo, sinp):
        self.nome_filme = nome_filme
        self.nome_filme_original = nome_filme_original
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento
        self.tipo = tipo
        self.sinopse = sinp
        self.premios = None

    def incluir_premios(self, premios):
        self.premios = premios


class Funcionario(ABC):
    @abstractmethod
    def __init__(self, nome, n_carteira, funcao, salario):
        self.nome = nome
        self.__n_carteira = n_carteira
        self.funcao = funcao
        self.salario = salario

    @abstractmethod
    def trabalhar(self):
        pass


class Pipoqueiro(Funcionario):
    def __init__(self, nome, n_carteira, funcao, salario):
        super().__init__(nome, n_carteira, funcao, salario)

    def trabalhar(self):
        print("Fazendo pipoca..")


class Projecionista(Funcionario):
    def __init__(self, nome, n_carteira, funcao, salario):
        super().__init__(nome, n_carteira, funcao, salario)

    def trabalhar(self):
        print("Projetando o filme..")


class AuxiliarLimpeza(Funcionario):
    def __init__(self, nome, n_carteira, funcao, salario):
        super().__init__(nome, n_carteira, funcao, salario)

    def trabalhar(self):
        print("Limpando a sala..")


# Programa Principal

# Cinema
cinema = Cinema("CineMais")

# Salas
sala1 = Sala(cinema, "Sala 1", 50)
sala2 = Sala(cinema, "Sala 2", 50)
sala3 = Sala(cinema, "Sala 3", 25)
sala4 = Sala(cinema, "Sala 4", 25)

# Filmes
filme1 = Filme("O Rei Leão (2019)", "Lion King (2019)", "Jon Favreau", 2019, "Musical", "Um filme sobre a savana africana.")
filme2 = Filme("O Silêncio dos Inocentes", "The Silence of the Lambs", "Jonathan Demme ", 1991, "Suspense", "Um filme sobre assasinos.")
filme3 = Filme("Django Livre", "Django Unchained", "Quentin Tarantino", 2012, "Ação", "Um filme sobre a escravidão.")

# Funcionários
func1 = Pipoqueiro("Jorge Irineu", 5634846954, "Faz pipocas", 1500)
func2 = Pipoqueiro("Leonardo Silva", 546513548, "Faz pipocas", 1500)
func3 = Projecionista("André Lucio", 54562135, "Projeta filmes", 2300)
func4 = Projecionista("Henrique Chaves", 5465674578, "Projeta filmes", 2300)
func5 = Projecionista("Thomas Leoncio", 546218624, "Projeta filmes", 2300)
func6 = Projecionista("Thomas Leoncio", 546235654, "Projeta filmes", 2300)
func7 = AuxiliarLimpeza("Quermes Gonzales", 546223498, "Auxiliar de Limpeza", 1300)

# Incluindo Sala em Cinema
cinema.incluir_salas(sala1)
cinema.incluir_salas(sala2)
cinema.incluir_salas(sala3)
cinema.incluir_salas(sala4)

# Incluindo Filme em Sala
sala1.passar_filme(filme1)
sala2.passar_filme(filme2)
sala3.passar_filme(filme3)
sala4.passar_filme(filme2)

# Definindo Premios
filme1.incluir_premios("Satellite Award: Melhor Filme de Animação | People's Choice Award: Dublagem de Animação Favorita")
filme2.incluir_premios("Oscar: Melhor Filme | Oscar: Melhor Roteiro Adaptado | Oscar: Melhor Diretor")
filme3.incluir_premios("Oscar: Melhor Roteiro Original | Oscar: Melhor Ator Coadjuvante para Christoph Waltz")

# Definindo horário das sessões

sala1.horario_exibicao("16:00")
sala1.horario_exibicao("17:00")
sala1.horario_exibicao("18:00")
sala2.horario_exibicao("20:00")
sala2.horario_exibicao("22:00")
sala2.horario_exibicao("23:00")
sala3.horario_exibicao("20:00")
sala3.horario_exibicao("23:00")
sala4.horario_exibicao("23:00")

# Incluindo os Funcionário nas salas
sala1.incluir_funcionarios(func1)
sala1.incluir_funcionarios(func3)
sala2.incluir_funcionarios(func2)
sala2.incluir_funcionarios(func4)
sala3.incluir_funcionarios(func5)
sala4.incluir_funcionarios(func6)
sala4.incluir_funcionarios(func7)

print(f"Nome do Cinema: {cinema.nome_cinema}")
print(f"Quantidade de salas oferecidas no cinema: {len(cinema.salas)}")
print(f"Nome das salas do cinema com suas respectivas capacidades: ", end="")
for i in cinema.salas:
    print(i.nome_sala, f"com {i.capaciade} cadeiras", end=" | ")
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------")

# Informações sobre a sala 1

print(f"Na {sala1.nome_sala}, sera apresentado o filme {sala1.filme.nome_filme} em {len(sala1.horario)} sessões.")
print(f"Horário das sessões: ", end="")
for i in sala1.horario:
    print(i, end=" | ")
print(" ")
print("Informações sobre o filme:")
print(f"Nome Original: {sala1.filme.nome_filme_original}")
print(f"Diretor: {sala1.filme.diretor}")
print(f"Ano de lançamento: {sala1.filme.ano_lancamento}")
print(f"Tipo: {sala1.filme.tipo}")
print(f"Sinópse: {sala1.filme.sinopse}")
print(f"Prêmios: {sala1.filme.premios}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
print(f"Funcionários escalados: {len(sala1.funcionarios)}")
print(f"Nome dos funcionários escalados: ", end="")
for i in sala1.funcionarios:
    print(i.nome, end=" | ")
print(" ")
for i in sala1.funcionarios:
    print(i.nome, "está ", end="")
    i.trabalhar()
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------")

# Informações sobre a sala 2

print(f"Na {sala2.nome_sala}, sera apresentado o filme {sala2.filme.nome_filme} em {len(sala2.horario)} sessões.")
print(f"Horário das sessões: ", end="")
for i in sala2.horario:
    print(i, end=" | ")
print(" ")
print("Informações sobre o filme:")
print(f"Nome Original: {sala2.filme.nome_filme_original}")
print(f"Diretor: {sala2.filme.diretor}")
print(f"Ano de lançamento: {sala2.filme.ano_lancamento}")
print(f"Tipo: {sala2.filme.tipo}")
print(f"Sinópse: {sala2.filme.sinopse}")
print(f"Prêmios: {sala2.filme.premios}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
print(f"Funcionários escalados: {len(sala2.funcionarios)}")
print(f"Nome dos funcionários escalados: ", end="")
for i in sala2.funcionarios:
    print(i.nome, end=" | ")
print(" ")
for i in sala2.funcionarios:
    print(i.nome, "está ", end="")
    i.trabalhar()
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------")

# Informações sobre a sala 3

print(f"Na {sala3.nome_sala}, sera apresentado o filme {sala3.filme.nome_filme} em {len(sala3.horario)} sessões.")
print(f"Horário das sessões: ", end="")
for i in sala3.horario:
    print(i, end=" | ")
print(" ")
print("Informações sobre o filme:")
print(f"Nome Original: {sala3.filme.nome_filme_original}")
print(f"Diretor: {sala3.filme.diretor}")
print(f"Ano de lançamento: {sala3.filme.ano_lancamento}")
print(f"Tipo: {sala3.filme.tipo}")
print(f"Sinópse: {sala3.filme.sinopse}")
print(f"Prêmios: {sala3.filme.premios}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
print(f"Funcionários escalados: {len(sala3.funcionarios)}")
print(f"Nome dos funcionários escalados: ", end="")
for i in sala3.funcionarios:
    print(i.nome, end=" | ")
print(" ")
for i in sala3.funcionarios:
    print(i.nome, "está ", end="")
    i.trabalhar()
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------")

# Informações sobre a sala 4

print(f"Na {sala4.nome_sala}, sera apresentado o filme {sala4.filme.nome_filme} em {len(sala4.horario)} sessões.")
print(f"Horário das sessões: ", end="")
for i in sala4.horario:
    print(i, end=" | ")
print(" ")
print("Informações sobre o filme:")
print(f"Nome Original: {sala4.filme.nome_filme_original}")
print(f"Diretor: {sala4.filme.diretor}")
print(f"Ano de lançamento: {sala4.filme.ano_lancamento}")
print(f"Tipo: {sala4.filme.tipo}")
print(f"Sinópse: {sala4.filme.sinopse}")
print(f"Prêmios: {sala4.filme.premios}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  ")
print(f"Quantidade de funcionários escalados: {len(sala4.funcionarios)}")
print(f"Nome dos funcionários escalados: ", end="")
for i in sala4.funcionarios:
    print(i.nome, end=" | ")
print(" ")
for i in sala4.funcionarios:
    print(i.nome, "está ", end="")
    i.trabalhar()
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------")
