# programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = int(input("Olá, para verificar se você pode votar, por favor, digite a sua idade: "))
if idade >= 16:
    print("Você pode votar!")
else:
    print("Você ainda não tem idade suficiente para votar!")