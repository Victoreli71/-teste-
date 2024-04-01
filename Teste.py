#constante da idade minima
IDADE_MINIMA = 18

#SOLICITE AO usuario que digite seu nome
nome = input("digite seu nome: ")

#solicite ao usuario que digite sua idade
idade = int(input("digite sua idade: ")) #convertendo  a idade em nmr inteiro

# solicite ao usuario que digite sua altura
altura = float(input(" digite sua altura em metros:")) #convertendo a altura em decimal

#solicite ao usuario que indique se deseja o serviço (true or false )
deseja_servico = input("voce deseja o serviço ? (sim ou não): ").lower()

#convertendo as entradas para minusculasvb

deseja_servico =  deseja_servico == "sim" # convertendo para booleano

# verifique se o usuario é maior de idade
maior_de_idade = idade >= IDADE_MINIMA

print(" ola", nome, "!")

if maior_de_idade:
    print("voce tem", idade, "anos, o que sig que pode adquirir o serviço")
else :
    print("voce tem", idade, "anos, o que significa que não pode adquirir o serviço ")