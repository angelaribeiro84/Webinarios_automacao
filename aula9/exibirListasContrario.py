def exibir_lista(lista, ao_contrario):

    if (ao_contrario == True):

        lista.reverse()

    for elemento_lista in lista:

        if len(str(elemento_lista)) > 0:

           print(elemento_lista, end=' / ')

    print()

estudantes = ['Alexander', 'Mia', 'Elijah', 'Noah', 'Emily', 'Charlotte', 'Mason']

idades_clientes = [19, 22, 42, 28, 69, 51, 18, 70]

equipe = ['Jordan Patel', '', 'Alex Kim', 'Taylor Nguyen', 'Jamie Singh', '', 'Avery Gonzalez', '', 'Casey Chen', '', 'Ydania', 'Angela', 'Eduardo', 'Marlon', 'Renan']

exibir_lista(lista=estudantes, ao_contrario=False)