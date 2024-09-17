# Solicita ao usuário para inserir dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if num1 > num2:
    print(f"O número {num1} é maior.")
elif num2 > num1:
    print(f"O número {num2} é maior.")
else:
    print("Os números são iguais.")
