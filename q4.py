# "Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123"
senha = "Python123"
senha_digitada = input("Por favor, digite a senha: ")
if senha_digitada == "Python123":
    print("Senha correta!")
else:
    print("Senha incorreta!")