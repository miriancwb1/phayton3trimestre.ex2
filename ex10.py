num = int(input("Digite um número inteiro não negativo: "))
fatorial = 1

if num < 0:
    print("Fatorial não definido para números negativos.")
else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é:", fatorial)