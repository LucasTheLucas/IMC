nome = input("Digite seu nome: ")
alturaCM = int(input("Digite sua altura em centimetros: "))
pesoKG = float(input("Digite seu peso em KG: "))
estado = ""
alturaM = alturaCM/100

imc = pesoKG / (alturaM*alturaM)

if imc < 18.5:
    estado = "Abaixo do peso (Pegue suplementos)"

elif imc >= 18.6 and imc <= 24.9: 
    estado = "Peso Ideal (Para Bens)"

elif imc >= 25 and imc <= 29.9:
    estado = "Sobre peso"

elif imc >= 30 and imc <= 34.9:
    estado = "Obesidade 1"

elif imc >= 35 and imc <= 39.9:
    estado = "Obesidade 2"

elif imc >= 40:
    estado = "Obesidade 3"

else:
    print("DADOS INVALIDOS INSERIDOS")

print(f"{nome}: {estado}")