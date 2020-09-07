# Tupla
tupla_carros = ("HRV", "Golf", "Argo")

lista_carros = list(tupla_carros)
lista_carros[2] = "Palio"
tupla_carros = tuple(lista_carros)

for x in tupla_carros:
    print(x)