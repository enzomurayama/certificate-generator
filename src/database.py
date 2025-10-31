import mysql.connector
from src.config import DB_CONFIG

def get_alunos_presentes():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM atividades;")
    total_atividades = cursor.fetchone()["total"]

    query = f"""
    SELECT 
        u.nome,
        COUNT(CASE WHEN ua.presente = 1 THEN 1 END) AS presencas,
        COUNT(ua.id) AS total_participacoes
    FROM userAtActivity ua
    JOIN users u ON u.id = ua.userId
    GROUP BY u.id
    HAVING (presencas / {total_atividades}) >= 0.75;
    """
    cursor.execute(query)
    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos
