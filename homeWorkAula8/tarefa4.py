'''O banco de dados contém as idades dos clientes. Descubra quantos
clientes têm mais de 21 anos, mas menos de 60.
clientes = [19, 22, 42, 28, 69, 51, 18, 70]
clientes_encontrados = 0
for ... in ...:
if ...:
clientes_encontrados = ...
print(clientes_encontrados)
Saída esperada: 4.
'''

clientes = [19, 22, 42, 28, 69, 51, 18, 70]
clientes_encontrados = 0
 
for cliente in clientes:
    if cliente > 21 and cliente < 60:
        clientes_encontrados = clientes_encontrados + 1

print(clientes_encontrados)