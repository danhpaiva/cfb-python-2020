# Tipos de dados em Python
x = 1  # inteiro
print("Valor da variável: ", x)
print("Tipo da variável: " + str(type(x)))  # Casting de type para string
print("---------------------------------")

x = "Paiva"  # string
print("Valor da variável: ", x)
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = 27.8  # float
print("Valor da variável: ", x)
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = True  # bool
print("Valor da variável: ", x)
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

numero1 = 5
numero2 = 10
x = complex(numero1, numero2)
print("Valor real: ", x.real)
print("Valor imaginário: ", x.imag)
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = ["Carro", "Avião", "Navio", 1, 27.2, False]  # List / Array
print("Valor: ", x[0])
print("Tipo da variável: " + str(type(x)))
x[0] = "Ônibus"
print("Valor: ", x[0])
print("---------------------------------")

# Tupla - n se modifica itens da tupla
x = ("Carro", "Avião", "Navio", 1, 27.2, False)
print("Valor: ", x[0])
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = range(0, 100, 1)
print("Valor: ", x[99])
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = {  # Dicionário
    "nome": "Paiva",
    "idade": 27,
    "vivo": True
}
print("Valor: ", x["nome"])
print("Vivo: ", x["vivo"])
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")

x = {  # SET - n repete valores
    1, 245, 178, 9, 1, 2, 2
}
print("Valor: ", x)
print("Tipo da variável: " + str(type(x)))
x = frozenset({1, 245, 178, 9, 1, 2, 2})
print("Valor: ", x)
print("Tipo da variável: " + str(type(x)))
print("---------------------------------")
