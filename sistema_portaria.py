from datetime import date

lista_pessoas = []

# Função para calcular a idade
def calcular_idade(dia, mes, ano):
    hoje = date.today()
    idade = hoje.year - ano

# Verifica se a pessoa já fez aniversário este ano
    if (hoje.month, hoje.day) < (mes, dia):
        idade -= 1
    return idade

#Função para validar a entrada, baseado na idade.
def validar_idade(idade):
    if idade >=18:
        return 'Entrada permitida!'
    else:  
        return 'Entrada proibida!'

while True:
    try:
        nome = input('Qual é o seu nome?')

        if not nome.replace(" ", "").isalpha():
            print('Digite apenas letras no nome!')
            continue

       # Entrada da data de nascimento
        dia = int(input('Digite o dia do nascimento: '))
        mes = int(input('Digite o mês do nascimento: '))
        ano = int(input('Digite o ano do nascimento: '))

        # Verifica se a data existe
        data_nascimento = date(ano, mes, dia)

        hoje = date.today()

        if data_nascimento > hoje:
            print("A data de nascimento não pode ser no futuro!")
            continue

        # Calcula idade automaticamente
        idade = calcular_idade(dia, mes, ano)

        print(f'Idade calculada: {idade} anos')

        resultado = validar_idade(idade)
        print(resultado)

        if resultado == 'Entrada permitida!':
            lista_pessoas.append(nome)

        continuar = input('Deseja cadastrar outra pessoa? (s/n): ')
        if continuar.lower() != 's':
            break

    except ValueError:
        print('Digite uma data válida!')

print('\nPessoas que entraram:')
for pessoa in lista_pessoas:
    print(pessoa)