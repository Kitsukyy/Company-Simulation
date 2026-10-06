from random import choice, randint
from time import sleep


class Empregado:
    numeros_empregados: int = 0

    def __init__(self):
        self.nome_completo: str = ""
        self.email: str = ""
        self.matricula_funcional = ""
        self.salario: int = 1600
        self.valor_horario: int = 150

    def iniciar_matricula(self):
        print("#  Vamos iniciar sua matricula! \n")
        while True:
            nome = input("Qual é o seu nome completo? \n").strip()
            if not nome:
                print("O nome não pode ficar vazio. Tente novamente. \n")
                continue
            elif any(caractere.isdigit() for caractere in nome):
                print("O nome não pode conter números. Tente novamente. \n")
                continue
            else:
                self.nome_completo = nome
                print("Nome cadastrado! \n")
                break
        while True:
            self.email = input("Por ultimo informe seu email : \n")
            if not self.email:
                print("O email não pode ficar vazio.")
                continue
            else:
                print("Email cadastrado! \n")
                self.criar_matricula_funcional()
                Empregado.contar_empregado()
                break

    @classmethod
    def contar_empregado(cls):
        cls.numeros_empregados += 1

    def criar_matricula_funcional(self):
        self.matricula_funcional = f"F{randint(0, 99999)}"

    def iniciar_jornada(self):
        self.trabalhador = self.nome_completo
        print(f"{self.trabalhador} iniciou o expediente. \n")
        self.horas_extras = randint(0, 6)
        self.horas = 6 + self.horas_extras
        sleep(self.horas)
        self.finalizar_jornada()

    def finalizar_jornada(self):
        print(f"{self.trabalhador} terminou o expediente. ")
        print(f"Terminou o expediente em {self.horas} Horas.")
        self.receber_salario()

    def receber_salario(self):
        salario = (self.salario * 1.00) + (self.horas_extras * self.valor_horario)
        print(f"O trabalhador {self.trabalhador} recebeu R$ {salario}. ")

    def receber_aumento(self):
        self.aumento = 0.10
        print("Parabens, você ira receber um aumento de 10%")


class GerenteProjeto(Empregado):
    porcentagem_aumento: float = 1.00

    def __init__(self):
        super().__init__()
        self.projetos: list = []
        self.time: list = []

    def iniciar_matricula(self):
        super().iniciar_matricula()
        print("Parabéns você se tornou um gerente! ")

    def receber_salario(self):
        salario = (self.salario * self.porcentagem_aumento) + (
            self.horas_extras * self.valor_horario
        )
        print(f"O gerente {self.trabalhador} recebeu R$ {salario}. ")

    def receber_aumento(self):
        super().receber_aumento()
        self.porcentagem_aumento += self.aumento

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.time.append(desenvolvedor)

    def remover_desenvolvedor(self, desenvolvedor: str):
        print(f"Removendo {desenvolvedor}...")
        try:
            self.time.remove(desenvolvedor)
        except ValueError:
            print(f"O {desenvolvedor} não existe. \n")
        else:
            print(f"O {desenvolvedor} foi removido com sucesso. \n")

    def participar_projeto(self):
        nome = input("Qual sera o nome do projeto? \n")
        while True:
            tempo = input("Será um projeto longo? [s/n] \n")
            if tempo.strip().capitalize() == "S":
                print(f'O projeto "{nome}" será um projeto longo. \n')
                self.projetos.append({"projeto": nome, "tempo": "Longo"})
                break
            elif tempo.strip().capitalize() == "N":
                print(f'O projeto "{nome}" será um projeto curto. \n')
                self.projetos.append({"projeto": nome, "tempo": "Curto"})
                break
            else:
                print("Resposta invalida, tente novamente.")
                continue

    def sair_projeto(self):
        nome = input("Qual sera o projeto removido? \n")
        while True:
            tempo = input("É um projeto longo? [s/n] \n")
            if tempo.strip().capitalize() == "S":
                try:
                    self.projetos.remove({"projeto": nome, "tempo": "Longo"})
                except ValueError:
                    print(
                        "Projeto não encontrado, você informou corretamente as informacões?"
                    )
                else:
                    print("O projeto foi removido. ")
                    break
            elif tempo.strip().capitalize() == "N":
                try:
                    self.projetos.remove({"projeto": nome, "tempo": "Curto"})
                except ValueError:
                    print(
                        "Projeto não encontrado, você informou corretamente as informacões?"
                    )
                else:
                    print("O projeto foi removido. ")
                    break
            else:
                print("Resposta invalida, tente novamente.")
                continue


class Desenvolvedor(Empregado):
    porcentagem_aumento: float = 1.00

    def __init__(self):
        super().__init__()
        self.linguagens_aprendidas: list = []
        self.cafe: float = 0
        self.burnout: bool = False
        self.linguagens_programacao = [
            "python",
            "C++",
            "C#",
            "C",
            "java",
            "php",
            "javascript",
            "html",
            "css",
        ]

    def iniciar_matricula(self):
        super().iniciar_matricula()
        print(f"Parabéns {self.nome_completo}, você se tornou um desenvolvedor! ")
        quantidade = len(gerentes)
        sorteio = randint(1, quantidade) - 1
        gerentes[sorteio].adicionar_desenvolvedor(self)
        print(f"Bem vindo ao time de {gerentes[sorteio].nome_completo}")

    def receber_salario(self):
        salario = (self.salario * self.porcentagem_aumento) + (
            self.horas_extras * self.valor_horario
        )
        print(f"O desenvolvedor {self.trabalhador} recebeu R$ {salario}. ")

    def receber_aumento(self):
        super().receber_aumento()
        self.porcentagem_aumento += self.aumento

    def aprender_linguagem(self):
        if not self.linguagens_programacao:
            print(f"{self.nome_completo} já aprendeu todas as linguagens!")
            return

        linguagem = choice(self.linguagens_programacao)
        self.linguagens_programacao.remove(linguagem)
        self.linguagens_aprendidas.append(linguagem)

        print(f"O desenvolvedor {self.nome_completo} aprendeu {linguagem}.")

    def verificar_linguagens(self):
        print(f"O Dev {self.nome_completo} possui as seguintes linguagens :")
        if not self.linguagens_aprendidas:
            print("Ele não sabe programar.")
        else:
            for linguagem in self.linguagens_aprendidas:
                print(linguagem)

    def beber_copo_cafe(self):
        print(f"O dev {self.nome_completo} bebeu um cafe")
        self.cafe += randint(100, 200)
        if self.cafe >= 2000:
            print(f"{self.nome_completo} teve um burnout! ")
            self.burnout = True

    def beber_cafeteira_cafe(self):
        print(f"O dev {self.nome_completo} bebeu a cafeteira toda!")
        self.cafe += randint(100, 1000)
        if self.cafe >= 2000:
            print(f"{self.nome_completo} teve um burnout! ")
            self.burnout = True

    def verificar_burnout(self):
        if self.burnout:
            print(f"O dev {self.nome_completo} está em burnout! ")
        else:
            print(f"O dev {self.nome_completo} está bem. ")


desenvolvedores = []
gerentes = []


def iniciar_simulacao():
    while True:
        emprego = input("Deseja procurar um emprego? [s/n] \n")
        if emprego == "s":
            while True:
                funcao = input("Deseja ser um dev ou gerente? [d/g] \n")
                if funcao == "d":
                    if not gerentes:
                        print("Não existe nenhum gerente para instruir lo")
                        break
                    else:
                        desenvolvedor = Desenvolvedor()
                        desenvolvedores.append(desenvolvedor)
                        print("Pedido feito, pode levar algum tempo para ser aceito. ")
                        sleep(3)
                        desenvolvedor.iniciar_matricula()
                        break
                elif funcao == "g":
                    gerente = GerenteProjeto()
                    gerentes.append(gerente)
                    print("Pedido feito, pode levar algum tempo para ser aceito. ")
                    sleep(3)
                    gerente.iniciar_matricula()
                    break
                else:
                    print("Resposta invalida, tente novamente.")
                    continue
        elif emprego == "n":
            print("Vagabundo! ")
            break
        else:
            print("Resposta invalida, tente novamente.")
            continue
        break
