### 10. Verifique se um número é divisível por 3 e 5
python
# Solicita ao usuário para inserir um número
num = int(input("Digite um número: "))

# Verifica se o número é divisível por 3 e 5
if num % 3 == 0 and num % 5 == 0:
    print(f"O número {num} é divisível por 3 e 5.")
else:
    print(f"O número {num} não é divisível por 3 e 5.")
