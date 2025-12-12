# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))
soma_numeros = primeiro_numero + segundo_numero
print(f"A soma dos números é {soma_numeros}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_divisao = int(input("Digite um número para ser dividido: "))
numero_divisor =  int(input("Digite um número divisor: "))
resto_divisao = numero_divisao % numero_divisor
print("Multiplicamos o resto por 5")
multiplicacao = resto_divisao * 5
print(f"O resultado é {multiplicacao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))
multiplicar_numeros = primeiro_numero * segundo_numero
print(f"O resultado da multiplicação dos números é {multiplicar_numeros}")

# #### Números de Ponto Flutuante (`float`)

# 4. Escreva um programa que receba dois números flutuantes e realize sua adição.
compras_janeiro = float(input("Digite o valor das compras de Janeiro: "))
compras_fevereiro = float(input("Digite o valor das compras de Fevereiro: "))
soma_compras = compras_janeiro + compras_fevereiro
print(f"Você gastou {soma_compras}")

# 5. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
avaliacao_a1 = float(input("Digite a sua nota da avaliação A1: "))
avaliacao_a2 = float(input("Digite a sua nota da avaliação A2: "))
media_notas = (avaliacao_a1 + avaliacao_a2) / 2 
print(f"Sua média foi {media_notas}")

# 6. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_potencia = float(input("Digite o valor fazemos o calculo da potência: "))
numero_expoente = float(input("Digite o expoente: "))
resultado_potencia = numero_potencia ** numero_expoente
print(f"O resultado da potência é {resultado_potencia}")

# #### Strings (`str`)

# 7. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome_user = input("Digite seu nome: ")
print(f"Seu nome em Maísculo fica {nome_user.upper()}")

# 8. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo_user = input("Digite seu nome completo: ")
print(f"Seu nome completo em Minusculo fica {nome_completo_user.lower()}")

# 9. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase_user = input("Digite uma frase: ")
print(f"Sua frase ficou {frase_user.strip()}")

# #### Booleanos (`bool`)

# 10. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
user_maior_idade = input("É maior de idade? (Digite True para sim ou False para não) ").lower()
user_dinheiro = input("Tem dinheiro? (Digite True para sim ou False para não) ").lower()
user_maior_idade = (user_maior_idade == "true")
user_dinheiro = (user_dinheiro == "true")
user_pode_comprar = user_maior_idade and user_dinheiro
print(f"Usúario pode beber? {user_pode_comprar}")

# 11. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
user_estuda = input("Você estuda programação? (Digite True para sim ou False para não) ").lower()
user_estuda = (user_estuda == "true")
print(f"Aqui consta que {not user_estuda}")

