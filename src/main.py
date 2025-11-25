from src.database import get_alunos_presentes
from src.certificado import gerar_certificado
from src.email_service import enviar_email_com_certificado

def main():
    print("📌 Escolha o tipo de cálculo de presença:")
    print("1 - Por horas")
    print("2 - Por atividades")

    opcao = input("Digite 1 ou 2: ").strip()

    if opcao == "1":
        tipo = "horas"
    elif opcao == "2":
        tipo = "atividades"
    else:
        print("❌ Opção inválida. Usando cálculo por horas.")
        tipo = "horas"

    # Modo teste
    print("\n📧 Deseja enviar o certificado APENAS para seu e-mail primeiro? (s/n)")
    modo_teste = input(">").lower().strip() == "s"

    if modo_teste:
        email_teste = input("Digite seu e-mail para teste: ").strip()
        print(f"🔧 Modo teste ativado! Certificados serão enviados somente para: {email_teste}\n")

    print(f"🔍 Buscando alunos usando o cálculo por {tipo}...\n")
    alunos = get_alunos_presentes(tipo=tipo)

    print(f"🎓 {len(alunos)} alunos encontrados. Gerando certificados...\n")
    for aluno in alunos:
        nome = aluno["nome"]
        email_destino = email_teste if modo_teste else aluno["email"]

        print(f"📄 Gerando certificado para: {nome}")
        caminho = gerar_certificado(nome)

        print(f"📧 Enviando certificado para: {email_destino}")
        enviar_email_com_certificado(
            destinatario=email_destino,
            nome_aluno=nome,
            caminho_certificado=caminho
        )

        print(f"✔️ Certificado enviado\n")

    print("\n✅ Todos os certificados foram gerados e enviados com sucesso!")

if __name__ == "__main__":
    main()
