notas = [1,2,3,4,5,6]

for valor in notas:
    print(valor)

string = 'Olá Mundo'

for caracter in string:
    print(caracter)

print(list(range(1, 10, 2)))

for num in range(0, 10):
    print(num)

num = 1
while num <= 9:
    print (num ** 2)
    num += 2


usuario_quiser = True

while usuario_quiser:
    usuario_input = input("Continuar? (S/N)")
    if usuario_input == "N":
        usuario_quiser = False