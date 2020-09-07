# Condicional If Elif Else
a = 10
b = 5
resultado = 0
operacao = "/"

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operador inválido")
print(str(a) + operacao + str(b) + " = " + str(resultado))

# ------------

clima = "sol"
dinheiro = 350
lugar = ""

if clima == "sol" and (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao " + lugar)
