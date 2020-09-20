import os
os.system("cls")

n1 = 10
n2 = 5


def somar():
    r = n1 + n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))


def subtrair():
    r = n1 - n2
    print("Subtração de " + str(n1) + " e " + str(n2) + " = " + str(r))


def calculos():
    somar()
    subtrair()


calculos()
