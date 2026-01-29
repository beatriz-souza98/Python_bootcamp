for n in range(10):
    print(f'O valor de n é: {n}')

for n in range(2):
    print('Olá')

valores = [1, 3, 5, 8]
for valor in valores:
    print(f'O valor é {valor}')
    print('Acabou o Loop')

nome = 'Marques'
for caractere in nome:
    print(f'O caractere é {caractere}')

clientes = [('Ana', 'xxxx', 'xxx@gmail.com'),
            ('José', 'xxxx', 'xxx@gmail.com')
            ]

for cliente in clientes:
    print(f'O nome é {cliente[0]}')
    print(f'Os dados do cliente são: \n Nome: {cliente[0]}\n Cpf: {cliente[1]} \n Email: {cliente[2]}')

for nome, cpf, email in clientes:
    print(f'Os dados do cliente são: \n Nome: {nome}\n Cpf: {cpf} \n Email: {email}')
