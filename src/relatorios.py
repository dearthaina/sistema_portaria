#Relatório final

def gerar_relatorio(registro_entrada, registro_saida):

    print("\n===== RELATÓRIO DE PERMANÊNCIA =====\n")

    print(
        f"{'CPF':15}"
        f"{'Nome':20}"
        f"{'Nascimento':15}"
        f"{'Entrada':22}"
        f"{'Saída':22}"
    )

    print("-" * 80)

    for entrada in registro_entrada:

        horario_saida = "Sem registro"

        for saida in registro_saida:

            if saida["Nome"] == entrada["Nome"]:
                horario_saida = saida["Saída"]

        print(

            f"{entrada['CPF']:15}"
            f"{entrada['Nome']:20}"
            f"{entrada['Nascimento']:15}"
            f"{entrada['Entrada']:22}"
            f"{horario_saida:22}"
        )