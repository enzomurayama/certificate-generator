from src.database import get_alunos_presentes
from src.certificado import gerar_certificado

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

    print(f"\n🔍 Buscando alunos usando o cálculo por {tipo}...\n")
    alunos = get_alunos_presentes(tipo=tipo)

    print(f"🎓 {len(alunos)} alunos encontrados. Gerando certificados...\n")
    for aluno in alunos:
        caminho = gerar_certificado(aluno["nome"])
        print(f"Certificado criado: {caminho}")

    print("\n✅ Todos os certificados foram gerados com sucesso!")

if __name__ == "__main__":
    main()
