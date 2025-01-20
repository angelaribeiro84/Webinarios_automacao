# Criar um novo arquivo chamado validarTamanho.py;

# Receber o nome do usuário;

# Se o tamanho do nome do usuário for maior que 3 caracteres, exiba:

# “Olá, {Nome}, cadastro realizado com sucesso!”

username = input()

username_length = len(username)

if(username_length > 3):

    print("Olá, "+ username + ", cadastro realizado com sucesso!")

else:

    print("Olá, "+ username + ", cadastro inválido, seu nome é muito pequeno :(")

# if(username_length > 3):

#     print(f"Olá, {username}, cadastro realizado com sucesso!")