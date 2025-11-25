import os
import mysql.connector
from src.config import DB_CONFIG


def get_total_atividades(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) 
        FROM atividades 
        WHERE categoriaId NOT IN (4, 5);
    """)
    total = cursor.fetchone()[0]
    cursor.close()
    return total


def query_presenca_por_horas(TOTAL_HORAS, LIMITE_PRESENCA):
    return f"""
        WITH presencas_deduplicadas AS (
            SELECT DISTINCT
                ua.userId,
                a.data,
                a.categoriaId,
                a.nome
            FROM userAtActivity ua
            JOIN atividades a ON a.id = ua.activityId
            WHERE ua.presente = 1
              AND a.categoriaId NOT IN (4, 5)
        )
        SELECT 
            u.nome,
            u.email,
            SUM(
                CASE 
                    WHEN pd.categoriaId = 1 THEN 4
                    WHEN pd.categoriaId = 2 THEN 1
                    WHEN pd.categoriaId = 3 AND LOWER(pd.nome) LIKE '%hackathon%' THEN 10
                    WHEN pd.categoriaId = 3 AND LOWER(pd.nome) LIKE '%maratona%' THEN 4
                    WHEN pd.categoriaId = 6 THEN 1
                    WHEN pd.categoriaId = 7 THEN 0.5
                    WHEN pd.categoriaId = 8 THEN 1
                    ELSE 0
                END
            ) AS horas_presentes
        FROM presencas_deduplicadas pd
        JOIN users u ON u.id = pd.userId
        GROUP BY u.id
        HAVING (horas_presentes / {TOTAL_HORAS}) >= {LIMITE_PRESENCA};
    """


def query_presenca_por_atividades(limite_minimo):
    return f"""
        WITH presencas_deduplicadas AS (
            SELECT DISTINCT
                ua.userId,
                a.id AS atividadeId
            FROM userAtActivity ua
            JOIN atividades a ON a.id = ua.activityId
            WHERE ua.presente = 1
              AND a.categoriaId NOT IN (4, 5)
        )
        SELECT 
            u.nome,
            u.email,
            COUNT(*) AS atividades_presentes
        FROM presencas_deduplicadas pd
        JOIN users u ON u.id = pd.userId
        GROUP BY u.id
        HAVING atividades_presentes >= {limite_minimo};
    """


def get_alunos_presentes(tipo="horas"):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    # Percentual exigido (padrão: 75%)
    LIMITE_PRESENCA = float(os.getenv("LIMITE_PRESENCA", 0.75))

    # Para cálculo por horas
    TOTAL_HORAS = int(os.getenv("TOTAL_HORAS_EVENTO", 45))

    total_atividades = get_total_atividades(conn)
    limite_atividades = int(total_atividades * LIMITE_PRESENCA)

    print(f"🔍 Modo de cálculo: {tipo}")

    if tipo == "horas":
        query = query_presenca_por_horas(TOTAL_HORAS, LIMITE_PRESENCA)
    elif tipo == "atividades":
        print(f"Total de atividades válidas: {total_atividades}")
        print(f"Mínimo exigido ({LIMITE_PRESENCA*100:.0f}%): {limite_atividades} atividades")
        query = query_presenca_por_atividades(limite_atividades)
    else:
        raise ValueError("Tipo inválido. Use 'horas' ou 'atividades'.")

    cursor.execute(query)
    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos
