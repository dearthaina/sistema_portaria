from datetime import date

lista_pessoas = []

# Regras de negócio: A entrada é permitida para pessoas acima de 18 anos.
def calcular_idade(dia, mes, ano):
    hoje = date.today()
    idade = hoje.year - ano

    if (hoje.month, hoje.day) < (mes, dia):
        idade -= 1
    return idade

def validar_idade(idade):
    if idade >=18:
        return 'Entrada permitida!'
    else:  
        return 'Entrada proibida!'

# Entrada de dados: Nome e data de nascimento

def obter_nome():     
    while True:
        nome = input('Qual é o seu nome?')

        if nome.replace(" ", "").isalpha():
            return nome
            
        print('Digite apenas letras no nome!')

def obter_data():

    while True:
        try:
            dia = int(input('Digite o dia do nascimento: '))
            mes = int(input('Digite o mês do nascimento: '))
            ano = int(input('Digite o ano do nascimento: '))

            data_nascimento = date(ano, mes, dia)

            hoje = date.today()

            if data_nascimento > hoje:
                print("A data de nascimento não pode ser no futuro!")
                continue

            return dia, mes, ano     

        except ValueError:
            print('Digite uma data válida!')

# Fluxo principal
while True:
    nome = obter_nome()
    dia, mes, ano = obter_data()

    idade = calcular_idade(dia, mes, ano)

    print(f'Idade calculada: {idade} anos')

    resultado = validar_idade(idade)
    print(resultado)

    if resultado == 'Entrada permitida!':
        lista_pessoas.append(nome)

    continuar = input('Deseja cadastrar outra pessoa? (s/n): ')
    if continuar.lower() != 's':
        break

print('\nPessoas que entraram:')
for pessoa in lista_pessoas:
    print(pessoa)