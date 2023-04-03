def diz_ola():
    print('Olá')

print(diz_ola())


ola = lambda : print('Olá')

# Lambda sempre em uma linha
a = lambda x: x**2
print(a(10))

soma = lambda x, y: x + y

print(soma(2,3))

impar_par = lambda x: print(f'{x} é Par') if x%2 == 0 else print(f'{x} é impar')
impar_par(11)