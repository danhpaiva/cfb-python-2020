class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()

c1.velMax = 100
c1.cor = "Azul"
c1.ligado = False
estado = "Sim" if c1.ligado else "Não"

print("Carro 01\n" + "Velocidade Máxima: " + str(c1.velMax) + "\nCor: " + c1.cor + "\nLigado: " + estado)