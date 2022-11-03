alcool = float(input("Preço do Álcool: "))
gasolina = float(input("Preço da Gasolina: "))

resultado = alcool/gasolina

print("Resultado do calculo: ", resultado)
print("")
if resultado <= 0.70:
    print("Está compensando abastecer com Álcool!")
else:
    print("Está compensando abastecer com Gasolina!")