#  programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

print("Olá, seja bem vindo(a)!")
nota = float(input("Para começar a verificação, digite sua nota: "))
if nota >= 6:
    print("Parabéns! Você foi aprovado(a)!")
elif nota <= 5:
    print("Você foi reprovado(a)!")
