class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self, vm, on, color):
        self.velMax = vm
        self.ligado = on
        self.cor = color

    def MostrarDados(self):
        estado = "Sim" if self.ligado else "Não"
        print("Velocidade Máxima: " + str(self.velMax) +
              "\nCor: " + self.cor + "\nLigado: " + estado)
        print()

    def LigarCarro(self):
        self.ligado = True

    def DesligarCarro(self):
        self.ligado = False

    def Andar(self):
        if(self.ligado):
            print("\tAndando...")
        else:
            print("\tCarro Desligado.")


c1 = Carro(200, False, "Preto")
c1.LigarCarro()
c1.MostrarDados()
c1.Andar()

c2 = Carro(50, False, "Vermelho")
c2.MostrarDados()
c2.Andar()

c3 = Carro(120, False, "Verde")
c3.MostrarDados()
