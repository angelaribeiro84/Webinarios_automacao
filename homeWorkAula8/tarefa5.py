'''A lista de equipe contém nomes de funcionários. Quando foi copiada do
banco de dados, algumas strings vazias apareceram, que não precisam
ser processadas. Você precisa encontrar um funcionário chamado Avery
Gonzalez. Complete o loop:
● Se um elemento da lista for uma string vazia, passe para o próximo
elemento. Para encontrar strings vazias, você precisará da função
len().
● Para cada elemento da lista, imprima 'Funcionário: [nome]'.
● Se o nome do funcionário for Avery Gonzalez, imprima 'Funcionário
Avery Gonzalez encontrado!' e interrompa o loop.
equipe = ['Jordan Patel', '', 'Alex Kim', 'Taylor Nguyen',
'Jamie Singh', '', 'Avery Gonzalez', '', 'Casey Chen', '']
for membro in equipe:
if ...
print(...)
if ...
Saída esperada:
Funcionário: Jordan Patel
Funcionário: Alex Kim
Funcionário: Taylor Nguyen
Funcionário: Jamie Singh
Funcionário: Avery Gonzalez
Funcionário Avery Gonzalez encontrado!'''


equipe = ['Jordan Patel', '', 'Alex Kim', 'Taylor Nguyen',
'Jamie Singh', '', 'Avery Gonzalez', '', 'Casey Chen', '']

for membro in equipe:

    if len(membro) == 0:
        continue
    print('Funcionário: ' + membro)


    if membro == 'Avery Gonzalez' :
        break

print('Funcionário', membro, 'encontrado!')