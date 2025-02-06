calories = {

  'Hambúrguer': 600,

  'Cheeseburger': 750,

  'Hambúrguer Vegetariano': 400,

  'Hambúrguer Vegano': 350,

  'Batatas Doces': 230,

  'Salada': 15,

  'Chá Gelado': 70,

  'Limonada': 90,

}

def contar_calorias(item_a, item_b, item_c): # declarando uma nova função

   

   soma_de_calorias = calories[item_a] + calories[item_b] + calories[item_c]

   

   return soma_de_calorias # retornando valores

 

soma_das_calorias = contar_calorias("Salada", "Cheeseburger", "Chá Gelado")

print(soma_das_calorias) # chamando uma nova função