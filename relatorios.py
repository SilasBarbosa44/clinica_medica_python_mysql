from conexao import conectar
from mysql.connector import Error


def listar_consulta():
    conn = conectar()
    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                p.nome AS paciente,
                m.nome AS medico,
                e.nome AS especialidade,
                c.data_consulta,
                c.valor AS valor_consulta
            FROM pacientes p
            INNER JOIN consultas c
                ON p.id_paciente = c.id_paciente
            INNER JOIN medicos m
                ON m.id_medico = c.id_medico
            INNER JOIN especialidades e
                ON m.id_especialidade = e.id_especialidade
            GROUP BY
                p.nome,
                m.nome,
                e.nome,
                c.valor,
                c.data_consulta;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def faturamento_medico():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                m.nome AS medico,
                COUNT(c.id_consulta) AS qtd_consultas,
                SUM(c.valor) AS faturamento
            FROM medicos m
            INNER JOIN consultas c
                ON m.id_medico = c.id_medico
            GROUP BY m.nome
            ORDER BY faturamento DESC;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def relatorio_por_especialidade():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                e.nome AS especialidade,
                COUNT(c.id_consulta) AS qtd_consultas,
                SUM(c.valor) AS faturamento,
                ROUND(SUM(c.valor) / COUNT(c.id_consulta),2) AS ticket_medio
            FROM consultas c
            INNER JOIN medicos m
                ON c.id_medico = m.id_medico
            INNER JOIN especialidades e
                ON m.id_especialidade = e.id_especialidade
            GROUP BY e.nome;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def relatorio_consultas_pagamentos():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                p.nome AS paciente,
                m.nome AS medico,
                e.nome AS especialidade,
                co.id_consultorio,
                c.data_consulta,
                pa.forma_pagamento,
                pa.status
            FROM pacientes p
            INNER JOIN consultas c
                ON p.id_paciente = c.id_paciente
            INNER JOIN consultorios co
                ON co.id_consultorio = c.id_consultorio
            INNER JOIN medicos m
                ON m.id_medico = c.id_medico
            INNER JOIN especialidades e
                ON e.id_especialidade = m.id_especialidade
            INNER JOIN pagamentos pa
                ON pa.id_consulta = c.id_consulta
            GROUP BY
                p.nome,
                m.nome,
                e.nome,
                co.id_consultorio,
                c.data_consulta,
                pa.forma_pagamento,
                pa.status
            ORDER BY paciente;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def ranking_medicos_por_faturamento():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                m.nome AS medico,
                SUM(c.valor) AS faturamento,
                RANK() OVER(
                    ORDER BY SUM(c.valor) DESC
                ) AS ranking
            FROM medicos m
            INNER JOIN consultas c
                ON m.id_medico = c.id_medico
            GROUP BY m.nome
            ORDER BY ranking;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()
def ranking_especialidade():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                e.nome AS especialidade,
                COUNT(c.id_consulta) AS qtd_consultas,
                DENSE_RANK() OVER(
                    ORDER BY COUNT(c.id_consulta) DESC
                ) AS ranking
            FROM consultas c
            INNER JOIN medicos m
                ON m.id_medico = c.id_medico
            INNER JOIN especialidades e
                ON e.id_especialidade = m.id_especialidade
            GROUP BY e.nome
            ORDER BY ranking;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def numeracao_consultas():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            SELECT
                data_consulta,
                ROW_NUMBER() OVER(
                    ORDER BY data_consulta
                ) AS ranking
            FROM consultas;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def comparacao_faturamento_pacientes():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            WITH pacientes AS (
                SELECT
                    p.nome AS paciente,
                    SUM(c.valor) AS faturamento
                FROM pacientes p
                INNER JOIN consultas c
                    ON p.id_paciente = c.id_paciente
                GROUP BY p.nome
            )

            SELECT
                paciente,
                faturamento,
                LAG(faturamento) OVER(
                    ORDER BY faturamento
                ) AS faturamento_anterior
            FROM pacientes;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()


def relatorio_pacientes():
    conn = conectar()

    try:
        if conn:
            cursor = conn.cursor()

            sql = """
            WITH relatorio_pacientes AS (

                SELECT
                    p.nome AS paciente,
                    p.email,
                    c.data_consulta,
                    SUM(c.valor) AS faturamento,
                    COUNT(DISTINCT c.id_consulta) AS qtd_consulta,
                    e.nome AS especialidade,
                    m.nome AS medico,
                    pa.forma_pagamento,
                    pa.data_pagamento,
                    pa.status

                FROM pacientes p

                INNER JOIN consultas c
                    ON c.id_paciente = p.id_paciente

                INNER JOIN medicos m
                    ON m.id_medico = c.id_medico

                INNER JOIN especialidades e
                    ON e.id_especialidade = m.id_especialidade

                INNER JOIN pagamentos pa
                    ON pa.id_consulta = c.id_consulta

                GROUP BY
                    p.nome,
                    p.email,
                    c.data_consulta,
                    e.nome,
                    m.nome,
                    pa.forma_pagamento,
                    pa.data_pagamento,
                    pa.status
            ),

            ranking_pacientes AS (

                SELECT
                    *,
                    DENSE_RANK() OVER(
                        ORDER BY faturamento DESC
                    ) AS ranking

                FROM relatorio_pacientes
            ),

            faturamento_anterior AS (

                SELECT
                    *,
                    LAG(faturamento) OVER(
                        ORDER BY faturamento
                    ) AS faturamento_anterior

                FROM ranking_pacientes
            ),

            crescimento_percentual AS (

                SELECT
                    *,
                    ROUND(
                        (faturamento - faturamento_anterior)
                        / NULLIF(faturamento_anterior,0) * 100,
                        2
                    ) AS crescimento_percentual

                FROM faturamento_anterior
            ),

            percentual_participacao AS (

                SELECT
                    *,
                    ROUND(
                        faturamento /
                        NULLIF(SUM(faturamento) OVER(),0) * 100,
                        2
                    ) AS percentual_participacao

                FROM crescimento_percentual
            ),

            classificacao_pacientes AS (

                SELECT
                    *,

                    CASE
                        WHEN faturamento >= 7000 THEN 'Valor alto'
                        WHEN faturamento >= 5000 THEN 'Valor medio'
                        ELSE 'Valor baixo'
                    END AS classificacao

                FROM percentual_participacao
            )

            SELECT *
            FROM classificacao_pacientes;
            """

            cursor.execute(sql)
            consulta = cursor.fetchall()

            for i in consulta:
                print(i)

            cursor.close()

    except Error as e:
        print(f"Erro ao listar consulta: {e}")

    finally:
        if conn:
            conn.close()