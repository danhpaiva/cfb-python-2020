# Coleção List
carros = ["Palio", "UNO", "Golf", "BMW"]

print(carros[0], carros[1])

print(carros[-1])

carros[3] = "Fusion"

print(carros[3])

carros.append("Fit")
carros.append("Polo")

print(carros)

print(str(len(carros)) + " Carros na lista")

carros.remove("Fusion")
print(str(len(carros)) + " Carros na lista")

del carros[0]
print(str(len(carros)) + " Carros na lista")

carros2 = list(carros)
print(str(len(carros)) + " Carros 2 na lista2")

carros.clear()
print(str(len(carros)) + " Carros na lista1")

carros3 = ["Fusca", "147", "Celta"]

carros4 = carros2 + carros3

print(carros4)
