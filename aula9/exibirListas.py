def exibir_lista(lista):
    for elemento_lista in lista:
        if len(str(elemento_lista)) > 0:
            print(elemento_lista)


estudantes = ['Alexander', 'Mia', 'Elijah', 'Noah', 'Emily', 'Charlotte', 'Mason']
idades_clientes = [19, 22, 42, 28, 69, 51, 18, 70] 
equipe = ['Jordan Patel', '', 'Alex Kim', 'Taylor Nguyen', 'Jamie Singh', '', 'Avery Gonzalez', '', 'Casey Chen', '', 'Ydania', 'Angela', 'Eduardo', 'Marlon', 'Renan']

exibir_lista(estudantes)
print('\n')
exibir_lista(idades_clientes)
print('\n')
exibir_lista(equipe)

