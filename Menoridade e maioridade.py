print("*********************************")
print("Segundo o Eca")
print("*********************************")

idade_str = input("Digite sua idade: ")

print("Você digitou", idade_str)

idade = int(idade_str)
adulto      = idade >  24
criança     = idade <  11
adolescente = idade >  12


if (adulto):
                 print("Você é maior de idade !.")
else:
    if (criança):
                 print("Você é uma criança !.")
    elif (adolescente):
                 print("Você é um adolescente !.")

                 print("Fim do jogo !")



