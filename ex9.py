# Solicita ao usuário para inserir uma nota
nota = float(input("Digite a nota (0 a 10): "))

# Verifica a classificação da nota
if nota >= 7:
    print("Aluno aprovado.")
elif 5 <= nota < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")