# Coletando os dados do usuário

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura**2

print("-" * 30)
print("Os dados coletados foram:")
print("Nome:", nome)
print("Idade:", idade , "anos")
print("Altura:", altura)
print("Peso:", peso , "kgs")
print("-" * 30)
print("IMC = ", imc)
print("")
if imc < 16:
    print("PALITO, SE VENTAR VOCÊ VOA!")
elif imc < 18.5:
    print("MUITO MAGRO, BORA FAZER UM PROJETINHO FELAS!")
elif imc < 24.90:
    print("TÁ NORMAL")
elif imc < 29.90:
    print("SOBREPESO, BORA COMEÇAR NO PROJETINHO EM!")
elif imc < 34.90:
    print("DIETA URGENTE!!!")
elif imc < 39.90:
    print("OBESO NIVEL 2")
else:
    print("SLC TIU DA UM JEITO AI PARCEIRO")
print("-" * 30)