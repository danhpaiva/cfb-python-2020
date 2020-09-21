# Declaração 01

soma = lambda a,b: a + b
mult = lambda a,b,c: (a+b) * c

print(soma(2,5))
print(mult(2,5,3))

# Declaração 02

print((lambda a,b: a+b)(3,2))

# Declaração 03

resultado = lambda x,func:x+func(x)
r = resultado(2,lambda x: x*x)
print(r)
r = resultado(2,lambda x: x+x)
print(r)