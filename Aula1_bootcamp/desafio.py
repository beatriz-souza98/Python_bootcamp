#Pedindo dados ao user
nome_usuario = input("Digite aqui seu nome: ")
salario_usuario = float(input("Digite o valor do seu salário: "))
bonus_usuario = float(input("Digite a porcentagem do seu bônus salarial: "))

#Calculo de Bônus
valor_do_bônus = 1000 + salario_usuario * bonus_usuario

#Saida para user
print(f"{nome_usuario} seu bônus salarial será de {valor_do_bônus} ")