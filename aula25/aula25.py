class NPC:  # Classe Base
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome: " + self.nome)
        print("Time: " + str(self.time))
        print("Força: " + str(self.forca))
        print("Munição: " + str(self.municao))
        print("Vivo: " + str("sim" if self.vivo else "Não"))
        print("Energia: " + str(self.energia))
        print("---")

class Soldado(NPC):
    # O construtor da classe filho sobrescreve o construtor da classe PAI
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        super().__init__(nome, time, self.forca, self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=100
        self.municao=20
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca=400
        self.municao=500
        super().__init__(nome, time, self.forca, self.municao)
    def informacao(self):
            super().info()

s1=Guarda("Olho Vivo", 1)
s2=Soldado("Bala na Agulha", 1)
s3=Elite("Ninja", 1)
s4=Guarda("Atento", 2)
s5=Soldado("Tiro Certo", 2)
s6=Elite("Samurai", 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.informacao()
