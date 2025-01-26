'''
Ao longo do dia, o conteúdo da sua bolsa pode mudar. Modifique a lista da bolsa.

Remova "pão" e adicione dois novos itens: "laptop" e "carregador". Substitua "chocolate" por "um pedaço de chocolate".

Use pop() e append().
'''

# A lista inicial que precisa ser modificada

bolsa = ["água", "pão", "chocolate", "chaves", "carteira", "fones de ouvido"]

# Remover "pão"

bolsa.pop(1)

# Adicionar "laptop"

bolsa.append("laptop")

# Adicionar "carregador"

bolsa.append("carregador")

# Substituir "chocolate" por "um pedaço de chocolate"

bolsa[2] = "um pedaço de chocolate"

print("A bolsa tem", bolsa)