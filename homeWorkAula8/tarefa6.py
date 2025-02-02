'''Imagine que você precisa automatizar um teste para a idade dos
passageiros do transporte público ao vender ingressos. Crianças com
menos de 5 anos de idade (não inclusivo) viajam de graça no transporte
público. Escreva um programa:
● Salve as idades elegíveis para uma viagem gratuita na lista
do_not_pay. Use apenas inteiros
● A variável idade armazena a idade do passageiro. Verifique se esse
valor está na lista do_not_pay. Atribua o teste à variável
resultado.
● Imprima o resultado.
# Preencha a lista com valores
do_not_pay = [....]
idade = int(input(“Insira a idade da criança”)) #cuidado ao
copiar com as aspas, talvez dê erro
# Atribua o teste à variável
resultado = ...
# Imprima o resultado
print(...)
Saída esperada: False'''

# Preencha a lista com valores
do_not_pay = [0, 1, 2, 3, 4]
idade = int(input()) #cuidado ao copiar com as aspas, talvez dê erro
# Atribua o teste à variável
Resultado = idade <= 5
# Imprima o resultado
print('A viagem é grátis?', bool(Resultado))