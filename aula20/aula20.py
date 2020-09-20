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
