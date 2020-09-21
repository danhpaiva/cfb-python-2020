valores = [1,2,3,4,5]

def somar(numero):
    resultado = 0
    for n in numero:
        resultado += n
    return resultado

print(str(valores) + " soma: " + str(somar(valores)))