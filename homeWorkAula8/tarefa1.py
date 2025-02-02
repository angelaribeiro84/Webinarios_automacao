#Imprima convites para todos os convidados da festa na lista. Para fazer isso, imprima todos os nomes da lista de amigos. Complete o loop para fazê-lo funcionar



amigos = ['Alexander', 'Mia', 'Elijah', 'Noah', 'Emily',
'Charlotte', 'Mason']


print("Estou organizando uma festa amanhã à noite!")

for amigo in amigos:
    if amigo != 'Mason' :

        print(amigo + ', eu te convido para minha casa!')
    else :
        print(amigo + ', eu te convido para minha casa!', end= '')
        print(' Vai ser divertido!')

print('\n')
print('\n')


#alternativa

print("Estou organizando uma festa amanhã à noite!")

for amigo in amigos:
    
    print(amigo + ', eu te convido para minha casa!')

    if amigo == "Mason" :

        break
        
    
print('Vai ser divertido!')    
