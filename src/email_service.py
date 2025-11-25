import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def enviar_email_com_certificado(destinatario, nome_aluno, caminho_certificado):
    remetente = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASS")

    assunto = "Seu certificado está pronto!"
    corpo = f"""
    Olá, {nome_aluno}!

    Apesar da demora, ele finalmente chegou! Seu certificado de participação está disponível em anexo.

    Esperamos que você tenha tido uma ótima experiência e contamos com sua presença no ano que vem 😊!

    Atenciosamente,

    Equipe da SECOMP
    """

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    nome_anexo = os.path.basename(caminho_certificado)

    # Anexar certificado
    with open(caminho_certificado, "rb") as f:
        pdf = MIMEApplication(f.read(), _subtype="pdf")
        pdf.add_header("Content-Disposition", "attachment", filename=nome_anexo)
        msg.attach(pdf)

    # Enviar
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())

    print(f"📧 Email enviado para {destinatario}")
