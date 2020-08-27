# Como usar o comando IF em Python
a = 10
b = 5
resultado = 0
operacao = "+"

if a > b:
    print("Verdadeiro")

print("Fim do programa!")

if a < b:
    print("Verdadeiro")

print("Fim do programa!")

if operacao == "+":
    resultado = a + b
if operacao == "-":
    resultado = a - b
if operacao == "*":
    resultado = a * b
if operacao == "/":
    resultado = a / b

print(str(a) + operacao + str(b) + " = " + str(resultado))
