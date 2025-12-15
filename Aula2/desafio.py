#Observar bugs que possam ocorrer

#Pedindo dados ao user
nome_usuario = input("Digite aqui seu nome: ")
#Solução caso usuário coloque numero
if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
# #Caso usuário não digite nada
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
# #Caso usuário coloque espaço e der enter
elif nome_usuario.isspace():
    print("Você digitou só espaço")
    exit()

salario = input("Digite o valor do seu salário: ")

#Caso usuario coloque virgula ao inves de ponto
salario = salario.replace(',', '.')
#Caso usuario digite letras
if salario.isalpha():
    print("Você digitou seu salário errado")
    exit()
#Caso usuário não digite nada
elif len(salario) == 0:
    print("Você digitou nada")
    exit()
#Caso usuário coloque espaço e der enter
elif salario.isspace():
    print("Você só deu espaço")
    exit()
salario_usuario = float(salario)

bonus = input("Digite a porcentagem do seu bônus salarial: ")
bonus = bonus.replace(',', '.')
#Caso usuario digite letras
if bonus.isalpha():
    print("Você digitou a porcentagem errada")
    exit()
#Caso usuário não digite nada
elif len(bonus) == 0:
    print("Você digitou nada")
    exit()
#Caso usuário coloque espaço e der enter
elif bonus.isspace():
    print("Você só deu espaço")
    exit()
#Caso usuario coloque simbolo da porcentagem
elif "%" in bonus:
    print("Digite apenas números") 
    exit()

bonus_usuario = float(bonus)
#Calculo de Bônus
valor_do_bônus = 1000 + salario_usuario * bonus_usuario

#Saida para user
print(f"{nome_usuario} seu bônus salarial será de {valor_do_bônus} ")