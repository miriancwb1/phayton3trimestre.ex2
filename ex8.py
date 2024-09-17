# Define a senha pré-definida
senha_correta = "senha123"

# Solicita ao usuário para inserir a senha
senha_usuario = input("Digite a sua senha: ")

# Verifica se a senha inserida é igual à senha pré-definida
if senha_usuario == senha_correta:
    print("A senha está correta.")
else:
    print("A senha está incorreta.")

