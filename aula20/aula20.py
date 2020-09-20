import os
os.system("cls")

def somar(*numero):
    r = 0

    for n in numero:
        r += n
    print("Soma: " + str(r))

somar(5,5,5,5,5)
somar(10,15)
somar(6,6,6,6,6,6,6,6,6,6,6,6,6,6)

def textos(*txt):
    for t in txt:
        print(t)


textos("Daniel", "Paiva", "Python")

textos("Linux", "Windows", "Mac", "Others")

def carros(c="Palio"):
    print("Modelo: " + c)

carros("HRV ")
carros()

valores = [1,3,5,10,2]

def multiplicar(numero):
    resultado = 1
    for n in numero:
        resultado *= n
    print("Multiplicação de valores da lista passada: " + str(resultado))

multiplicar(valores)