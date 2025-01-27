# Agora você precisa exibir informações mais detalhadas sobre eles. As variáveis passed e failed são fornecidas como entrada.
passed = 3
failed = '2'

count = print(passed + int(failed)) # Aqui você precisa calcular o número total de testes realizados
message_result = 'Completed ' + str(count) + ' tests'
message_details = 'Successfully completed: ' + str(passed) + ', failed: ' + (failed)
print(message_result)
print(message_details)