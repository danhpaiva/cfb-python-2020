import os
os.system("cls")

carro = {"Fabricante": "Honda",
         "Modelo": "HRV",
         "Ano": "2016",
         "Cor": "Prata"}  # Chave/Key - Valor/Value

print(carro)
print(carro["Modelo"])
print(carro["Cor"])

fab = carro.get("Fabricante")
print(fab)

print()

carro["Cor"] = "Preto"  # ALterar cor
print(carro["Cor"])
print()

# Imprimir Chave
for x in carro:
    print(x)
print()

# Imprimir Valor
for x in carro:
    print(carro[x])
print()

for chave, valor in carro.items():  # Percorrer chave e valor
    print(chave + ": " + valor)
print()

if "Modelo" in carro:
    print("Modelo é uma chave \n")
print()

print("Tamanho do Dictionary: " + str(len(carro)))  # Tamanho dic
print()

carro["Cambio"] = "Automático"  # Add nova chave e valor
print(carro)
print()

carro.pop("Cambio")  # Remover chave
print(carro)
print()

carro.clear()  # Limpar Dic
print("Tamanho do dic:" + str(len(carro)))

os.system("cls")

veiculos = {
    "Carro1": {
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },
    "Carro2": {
        "Fabricante": "Fiat",
        "Modelo": "Palio"
    },
    "Carro3": {
        "Fabricante": "Ford",
        "Modelo": "Focus"
    }
}

print(veiculos)
print(veiculos["Carro3"])
print(veiculos["Carro3"]["Modelo"])

veiculo1 = {
    "Fabricante": "Honda",
    "Modelo": "HRV"
}

veiculo2 = {
    "Fabricante": "Fiat",
    "Modelo": "Palio"
}

veiculo3 = {
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

todosVeiculos = {
    "V1": veiculo1,
    "V2": veiculo2,
    "V3": veiculo3
}

print(todosVeiculos["V1"])
