sistema_portaria
#Função para validar a idade, reconhecendo se é maior de 18 anos ou não.
def validar_idade(idade):
    if idade >=18:
        return 'Entrada permitida!'
    else:  
        return 'Entrada proibida!'
#Loop para verificação de caracteres
while True:
    try:    
        idade=int(input('Qual é a sua idade?'))
        print(validar_idade(idade))
        break
    except ValueError:
        print('Digite um número valido!')