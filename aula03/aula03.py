# Variáveis em Python
num1 = num2 = resultado = 0
nome = "Paiva"


def ChamarNome():
    global idade 
    idade = 27
    print(nome)


ChamarNome()
print(idade)
