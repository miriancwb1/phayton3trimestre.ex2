# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar usando o operador de módulo
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")