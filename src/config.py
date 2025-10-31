import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

CERT_CONFIG = {
    "modelo": os.getenv("CERT_MODEL_PATH", "./modelo_certificado.png"),
    "saida": os.getenv("CERT_OUTPUT_DIR", "./certificados"),
    "fonte": os.getenv("FONT_PATH", "./Inter-SemiBold.ttf"),
    "tamanho_fonte": int(os.getenv("FONT_SIZE", "96")),
    "cor_texto": tuple(map(int, os.getenv("FONT_COLOR", "255,255,255").split(","))),
    "posicao": tuple(map(int, os.getenv("TEXT_POS", "2100,2900").split(","))),
}
