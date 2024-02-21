# Programa para calcular IMC
# Desenvolvido por Celso

print("**************************************")
print("*         CALCULADORA IMC            *")
print("**************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS

nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DE DADOS

nome = input("Digite seu nome? ")
peso = int(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC

imc = peso / (altura * altura)

#SAÍDA DO PROCESSAMENTO
print()
print("***************************************")
print("*              RESULTADO              *")
print("***************************************")
print("*                                     *")
print("Nome: " + nome)
print("Peso: " + str(peso))
print("Altura: " + str(altura))
print("IMC: " + str(imc))
print("***************************************")



