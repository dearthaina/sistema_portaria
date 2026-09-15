from datetime import date, datetime
from relatorios import gerar_relatorio

#Armazenamento de registros
registro_entrada = []
registro_saida = []

# Regras de negócio: A entrada é permitida para pessoas acima de 18 anos.
def calcular_idade(dia, mes, ano):
    hoje = date.today()
    idade = hoje.year - ano

    if (hoje.month, hoje.day) < (mes, dia):
        idade -= 1
    return idade

def validar_idade(idade):
    if idade >=18:  
        return True
    
# Entrada de dados: Nome e Data de nascimento

def obter_nome():     
    while True:
        nome = input('Digite o Nome e último Sobrenome: ')

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

            return data_nascimento     

        except ValueError:
            print('Digite uma data válida!')

#Registrar horário     

def registrar_horario():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Registrar entrada

def registrar_entrada():

    print("\n===== REGISTRO DE ENTRADA =====")

    nome = obter_nome()

    data_nascimento = obter_data()

    idade = calcular_idade(
        data_nascimento.day,
        data_nascimento.month,
        data_nascimento.year
    )

    if validar_idade(idade):

        pessoa = {
            "Nome": nome,
            "Nascimento": data_nascimento.strftime("%d/%m/%Y"),
            "Entrada": registrar_horario()
        }

        registro_entrada.append(pessoa)

        print("\nEntrada permitida!")
        print("Entrada registrada com sucesso.")

    else:
        print("\nEntrada proibida!")
        print("Usuário não possui idade permitida.")

# Registrar saída

def registrar_saida():

    print("\n===== REGISTRO DE SAÍDA =====")

    if not registro_entrada:

        print("Não existem pessoas registradas no local.")

        return

    print("\nPessoas presentes:")

    for indice, pessoa in enumerate(registro_entrada, start=1):

        print(f"{indice} - {pessoa['Nome']}")

    escolha = int(
        input("\nDigite o número da pessoa que saiu: ")
    )

    pessoa = registro_entrada[escolha - 1]

    saida = {

        "Nome": pessoa["Nome"],
        "Saída": registrar_horario()
    }

    registro_saida.append(saida)

    print("\nSaída registrada com sucesso!")

def main():

    while True:

        print("\n===== SISTEMA DE CONTROLE DE ACESSO =====")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Gerar relatório")
        print("4 - Sair")

        opcao = input("\nDigite uma opção: ")

        if opcao == "1":
            registrar_entrada()

        elif opcao == "2":
            registrar_saida()

        elif opcao == "3":
            gerar_relatorio(registro_entrada, registro_saida)

        elif opcao == "4":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Digite uma opção de 1 a 4.")

main()