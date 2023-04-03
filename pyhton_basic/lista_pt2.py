minha_lista = [0,1,2,3,4] 

print([x for x in range(5)])
print([x**2 for x in range(5)])

#somente os pares
print([x for x in range(10) if x % 2 == 0])

pessoas_conhecidas = ['Ana', ' Manuela', 'felipe', 'PEDRO']

pessoas_padrao = [pessoa.strip().capitalize() for pessoa in pessoas_conhecidas]
print(pessoas_padrao)