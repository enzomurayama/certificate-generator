import os
import mysql.connector
from src.config import DB_CONFIG

def get_alunos_presentes():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    TOTAL_HORAS = int(os.getenv("TOTAL_HORAS_EVENTO", 45))
    LIMITE_PRESENCA = float(os.getenv("LIMITE_PRESENCA", 0.70))

    print(f"🕒 Total de horas possíveis: {TOTAL_HORAS}")

    query = f"""
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

    cursor.execute(query)
    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos
