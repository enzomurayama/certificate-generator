import os
from PIL import Image, ImageDraw, ImageFont
from src.config import CERT_CONFIG

def gerar_certificado(nome):
    modelo_certificado = CERT_CONFIG["modelo"]
    pasta_saida = CERT_CONFIG["saida"]
    fonte_ttf = CERT_CONFIG["fonte"]
    tamanho_fonte = CERT_CONFIG["tamanho_fonte"]
    cor_texto = CERT_CONFIG["cor_texto"]
    posicao_nome = CERT_CONFIG["posicao"]

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    fonte = ImageFont.truetype(fonte_ttf, tamanho_fonte)
    img = Image.open(modelo_certificado).convert("RGBA")
    draw = ImageDraw.Draw(img)

    x = posicao_nome[0]
    y = posicao_nome[1]

    draw.text((x, y), nome, font=fonte, fill=cor_texto)
    caminho_saida = os.path.join(pasta_saida, f"{nome}.png")
    img.save(caminho_saida)
    return caminho_saida
