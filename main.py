from conexao import conectar
from crud import *
from relatorios import *
from menu import menu


def main():
    conn = conectar()

    if conn is None:
        return

    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome paciente que deseja cadastrar: ")
            cpf = input("Digite o CPF: ")
            data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
            sexo = input("Digite o sexo [M/F]: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            cidade = input("Digite a cidade: ")
            endereco = input("Digite o endereço: ")
            data_cadastro = input("Digite a data de cadastro (AAAA-MM-DD): ")

            cadastrar_paciente(
                conn,
                nome,
                cpf,
                data_nascimento,
                sexo,
                telefone,
                email,
                cidade,
                endereco,
                data_cadastro,
            )

        elif opcao == "2":
            listar_pacientes(conn)

        elif opcao == "3":
            try:
                id_paciente = int(input("Digite o ID do paciente: "))
                nome = input("Digite o nome: ")
                cpf = input("Digite o CPF: ")
                data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
                sexo = input("Digite o sexo [M/F]: ")
                telefone = input("Digite o telefone: ")
                email = input("Digite o email: ")
                cidade = input("Digite a cidade: ")
                endereco = input("Digite o endereço: ")
                data_cadastro = input("Digite a data de cadastro (AAAA-MM-DD): ")

                atualizar_paciente(
                    conn,
                    id_paciente,
                    nome,
                    cpf,
                    data_nascimento,
                    sexo,
                    telefone,
                    email,
                    cidade,
                    endereco,
                    data_cadastro,
                )
            except ValueError:
                print("Digite apenas números para o ID!")

        elif opcao == "4":
            try:
                id_paciente = int(input("Digite o ID do paciente: "))
                excluir_paciente(conn, id_paciente)
            except ValueError:
                print("Digite apenas números para o ID!")

        elif opcao == "5":
            nome = input("Digite o nome do médico: ")
            crm = input("Digite o CRM: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")

            try:
                salario = float(input("Digite o salário: "))
                data_admissao = input("Digite a data de admissão (AAAA-MM-DD): ")
                id_especialidade = int(input("Digite o ID da especialidade: "))

                cadastrar_medico(
                    conn,
                    nome,
                    crm,
                    telefone,
                    email,
                    salario,
                    data_admissao,
                    id_especialidade,
                )
            except ValueError:
                print("Digite valores numéricos válidos!")

        elif opcao == "6":
            listar_medicos(conn)

        elif opcao == "7":
            try:
                id_paciente = int(input("ID do paciente: "))
                id_medico = int(input("ID do médico: "))
                id_consultorio = int(input("ID do consultório: "))
                data_consulta = input("Data (AAAA-MM-DD): ")
                horario = input("Horário (HH:MM): ")
                valor = float(input("Valor: "))
                status = input("Status: ")
                observacoes = input("Observações: ")

                agendar_consulta(
                    conn,
                    id_paciente,
                    id_medico,
                    id_consultorio,
                    data_consulta,
                    horario,
                    valor,
                    status,
                    observacoes,
                )
            except ValueError:
                print("Digite valores numéricos válidos!")

        elif opcao == "8":
            try:
                id_consulta = int(input("Digite o ID da consulta: "))
                status = input("Digite o novo status (ex: Cancelada): ")
                cancelar_consulta(conn, status, id_consulta)
            except ValueError:
                print("Digite apenas números para o ID!")

        elif opcao == "9":
            listar_consultas(conn)

        elif opcao == "10":
            try:
                id_consulta = int(input("Digite o ID da consulta: "))
                forma_pagamento = input("Forma de pagamento: ")
                valor = float(input("Valor: "))
                data_pagamento = input("Data (AAAA-MM-DD): ")
                status = input("Status: ")

                registrar_pagamentos(
                    conn,
                    id_consulta,
                    forma_pagamento,
                    valor,
                    data_pagamento,
                    status,
                )
            except ValueError:
                print("Digite valores numéricos válidos!")

        elif opcao == "11":
            listar_consulta(conn)

        elif opcao == "12":
            faturamento_medico(conn)

        elif opcao == "13":
            relatorio_por_especialidade(conn)

        elif opcao == "14":
            relatorio_consultas_pagamentos(conn)

        elif opcao == "15":
            ranking_medicos_por_faturamento(conn)

        elif opcao == "16":
            ranking_especialidade(conn)

        elif opcao == "17":
            numeracao_consultas(conn)

        elif opcao == "18":
            comparacao_faturamento_pacientes(conn)

        elif opcao == "19":
            relatorio_pacientes(conn)

        elif opcao == "0":
            print("Sistema encerrado!")
            conn.close()
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()