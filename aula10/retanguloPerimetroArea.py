def recuperar_medidas_retangulo( lado_a, lado_b ):

    

    perimetro = (lado_a*2) + (lado_b*2)

    area = lado_a * lado_b 

    

    return perimetro , area

lado_a = int(input('Valor do lado a: '))

lado_b = int(input('Valor do lado b: '))

print('A medida do retangulo e:', recuperar_medidas_retangulo(lado_a, lado_b))