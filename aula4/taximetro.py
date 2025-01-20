# 1. Criar um novo arquivo chamado taximetro.py;
# 2. Receber a quantidade de km rodados pelo táxi;
# 3. Receber o preço por km do táxi;
# 4. Receber a taxa fixa do táxi;
# 5. Exibir o preço total da corrida.


quantidade_km_rodado = float (input())
preco_km = float (input())
taxa_fixa_km = float (input())

print("O preco total da corrida foi:", quantidade_km_rodado * preco_km + taxa_fixa_km)
