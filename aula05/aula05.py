# Tipos numéricos, random e operações de casting
import random

num_i = 10
num_f = 5.5
num_c = 1j

x = num_i
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = num_f
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = num_c
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = int(num_f)
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = float(num_i)
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

num_r = random.randrange(0, 59)
x = num_r
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

num_r = [
    random.randrange(0, 59)
    , random.randrange(0, 59)
    , random.randrange(0, 59)
    , random.randrange(0, 59)
    , random.randrange(0, 59)
    , random.randrange(0, 59)
]
print(num_r)
print("Valor 1: " + str(num_r[0]) + " - Tipo: " + str(type(num_r[0])))
print("Valor 6: " + str(num_r[5]) + " - Tipo: " + str(type(num_r[5])))