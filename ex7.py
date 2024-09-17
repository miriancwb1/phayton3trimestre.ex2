# Solicita ao usuário para digitar uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se a letra é vogal ou consoante
if letra in 'aeiou':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")
a