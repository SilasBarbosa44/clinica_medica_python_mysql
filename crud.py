from mysql.connector import Error


def cadastrar_paciente(
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
):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            INSERT INTO pacientes
            (nome, cpf, data_nascimento, sexo, telefone, email, cidade, endereco, data_cadastro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
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
            cursor.execute(sql, valores)
            conn.commit()
            print("Paciente cadastrado com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao cadastrar paciente: {e}")


def listar_pacientes(conn):
    try:
        if conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM pacientes"
            cursor.execute(sql)
            pacientes = cursor.fetchall()

            if not pacientes:
                print("Nenhum paciente encontrado!")
            else:
                for paciente in pacientes:
                    print(paciente)

            cursor.close()
    except Error as e:
        print(f"Erro ao listar pacientes: {e}")


def atualizar_paciente(
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
):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            UPDATE pacientes
            SET nome = %s, cpf = %s, data_nascimento = %s, sexo = %s, 
                telefone = %s, email = %s, cidade = %s, endereco = %s, data_cadastro = %s
            WHERE id_paciente = %s
            """
            valores = (
                nome,
                cpf,
                data_nascimento,
                sexo,
                telefone,
                email,
                cidade,
                endereco,
                data_cadastro,
                id_paciente,
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("Paciente atualizado com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao atualizar paciente: {e}")


def excluir_paciente(conn, id_paciente):
    try:
        if conn:
            cursor = conn.cursor()
            sql = "DELETE FROM pacientes WHERE id_paciente = %s"
            valores = (id_paciente,)
            cursor.execute(sql, valores)
            conn.commit()
            print("Paciente excluído com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao excluir paciente: {e}")


def cadastrar_medico(
    conn, nome, crm, telefone, email, salario, data_admissao, id_especialidade
):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            INSERT INTO medicos
            (nome, crm, telefone, email, salario, data_admissao, id_especialidade)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                nome,
                crm,
                telefone,
                email,
                salario,
                data_admissao,
                id_especialidade,
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("Médico cadastrado com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao cadastrar médico: {e}")


def listar_medicos(conn):
    try:
        if conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM medicos"
            cursor.execute(sql)
            medicos = cursor.fetchall()

            if not medicos:
                print("Nenhum médico encontrado!")
            else:
                for medico in medicos:
                    print(medico)

            cursor.close()
    except Error as e:
        print(f"Erro ao listar médicos: {e}")


def agendar_consulta(
    conn,
    id_paciente,
    id_medico,
    id_consultorio,
    data_consulta,
    horario,
    valor,
    status,
    observacoes,
):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            INSERT INTO consultas
            (id_paciente, id_medico, id_consultorio, data_consulta, horario, valor, status, observacoes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                id_paciente,
                id_medico,
                id_consultorio,
                data_consulta,
                horario,
                valor,
                status,
                observacoes,
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("Consulta agendada com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao agendar consulta: {e}")


def cancelar_consulta(conn, status, id_consulta):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            UPDATE consultas
            SET status = %s
            WHERE id_consulta = %s
            """
            valores = (status, id_consulta)
            cursor.execute(sql, valores)
            conn.commit()
            print("Status da consulta atualizado com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao cancelar consulta: {e}")


def listar_consultas(conn):
    try:
        if conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM consultas"
            cursor.execute(sql)
            consultas = cursor.fetchall()

            if not consultas:
                print("Nenhuma consulta cadastrada!")
            else:
                for consulta in consultas:
                    print(consulta)

            cursor.close()
    except Error as e:
        print(f"Erro ao listar consultas: {e}")


def registrar_pagamentos(
    conn, id_consulta, forma_pagamento, valor, data_pagamento, status
):
    try:
        if conn:
            cursor = conn.cursor()
            sql = """
            INSERT INTO pagamentos
            (id_consulta, forma_pagamento, valor, data_pagamento, status)
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                id_consulta,
                forma_pagamento,
                valor,
                data_pagamento,
                status,
            )
            cursor.execute(sql, valores)
            conn.commit()
            print("Pagamento registrado com sucesso!")
            cursor.close()
    except Error as e:
        print(f"Erro ao registrar pagamento: {e}")