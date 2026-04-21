lista_pessoas = []

#Função para validar a idade, reconhecendo se é maior de 18 anos ou não.
def validar_idade(idade):
    if idade >=18:
        return 'Entrada permitida!'
    else:  
        return 'Entrada proibida!'

while True:
    try:
        nome = input('Qual é o seu nome?')
        idade = int(input('Qual é a sua idade?'))

        resultado = validar_idade(idade)
        print(resultado)

        if resultado == 'Entrada permitida!':
            lista_pessoas.append(nome)

        continuar = input('Deseja cadastrar outra pessoa? (s/n): ')
        if continuar.lower() != 's':
            break

    except ValueError:
        print('Digite um número válido!')

print('\nPessoas que entraram:')
for pessoa in lista_pessoas:
    print(pessoa)