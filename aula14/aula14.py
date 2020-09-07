# Loop While
import os
os.system("cls")  # limpar console

# Possibilidade 01
i = 0
while i < 10:
    print(i)
    i += 1
print("Fim do loop")

# Possibilidade 02
os.system("cls")

i = 0
while i < 10:
    print(i)
    i += 1
    if(i >= 5):
        break
print("Fim do loop")

# Possibilidade 03
os.system("cls")

carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]

tamanho = len(carros)
i = 0

while i < tamanho:
    print(carros[i])
    i += 1
print("\nFim do loop")

# Possibilidade 04
os.system("cls")

carros = []
carro = input("Digite o nome do novo carro: ")

while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

print(carros)
print("\nFim do loop")
