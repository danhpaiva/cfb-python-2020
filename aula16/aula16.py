# Matrizes
carros = [
    ["Modelo", "HRV"], 
    ["Fabricante", "Honda"], 
    ["Ano", 2020]
]

carros.append(["Cor", "Prata"])

print(carros[0][0])
print(carros[0][1])
print(carros[1][1])

for linha, coluna in carros:
    print("Linha: " + linha + " | " + "Coluna: " + str(coluna))