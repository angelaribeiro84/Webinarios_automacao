#Crie uma variável com o valor “Amsterdam”. Imprima todas as letras uma a uma, pulando as letras “A”.

cidade = 'Amsterdam'

for letra in cidade:

    if letra == 'a' or letra == 'A': 

        continue

    print ('Letra Atual:', letra)

print ("Não imprimimos A!")