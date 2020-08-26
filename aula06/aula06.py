# Strings P1
curso = "Curso de Python"

print(curso[0])
print(curso[0:5])
print(curso[9:15])
print("Tamanho: " + str(len(curso)))

nome = " Paiva "
print(nome)
print(nome.strip())
print(nome.lower())
print(nome.upper())
print(nome.upper().strip())
print(curso.replace("Python", "C#"))

a = curso.split(" ")
print(a[0])
print(a[1])
print(a[2])