'''O departamento de desenvolvimento possui duas equipes: testadores e
desenvolvedores. Imprima os nomes de todos os funcionários do
departamento.

Saída esperada:
Funcionários:
Jordan Lee
Alex Patel
Taylor Nguyen
Casey Johnson
'''

equipe_qa = ['Jordan Lee', 'Alex Patel']
equipe_dev = ['Taylor Nguyen', 'Casey Johnson']
departamento = equipe_qa + equipe_dev

print('Funcionários:')
for qa_func in equipe_qa :
    print(qa_func)

for dev_func in equipe_dev :
    print(dev_func)