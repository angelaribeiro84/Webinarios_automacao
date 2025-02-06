'''Calcule o preço do produto com base na quantidade.

Preços dos produtos: 

"leite": 10,
"pão": 5,
"manteiga": 15
Exiba os dados assim: 

“Você precisa pagar: XXX” (X = preço do produto * quantidade)'''

def recuperar_preco_dos_produtos(produto, quantidade):

    preco_produtos = {

        "leite" : 10,
        "pao" : 5,
        "manteiga" : 15
    }

    valor_total = quantidade * preco_produtos[produto]

    return valor_total

 

produto = input('Qual produto você deseja?  ')

quantidade = int(input('Quanto desse produto você deseja?  '))

print("Você precisa pagar:", recuperar_preco_dos_produtos(produto, quantidade))