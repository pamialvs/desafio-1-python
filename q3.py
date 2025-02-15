#  criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

print("Seja bem vindo(a)!")
nota = float(input("Para começar a converssão digite a sua nota: "))
if nota >= 90 and nota <=100:
    print("Parabéns, você tirou A!")
elif nota >=80 and nota <=89:
    print("Muito bem, você tirou B.")
elif nota >= 70 and nota <= 79:
    print("Bom trabalho, você tirou C.")
elif nota >= 60 and nota <= 69:
    print("Fique atento, você tirou D.")
elif nota <= 60:
    print("Estude um pouco mais, você tirou F.")