from src.database import get_alunos_presentes
from src.certificado import gerar_certificado

def main():
    print("🔍 Buscando alunos com mais de 75% de presença...")
    alunos = get_alunos_presentes()

    print(f"🎓 {len(alunos)} alunos encontrados. Gerando certificados...\n")
    for aluno in alunos:
        caminho = gerar_certificado(aluno["nome"])
        print(f"Certificado criado: {caminho}")

    print("\n✅  Todos os certificados foram gerados com sucesso!")

if __name__ == "__main__":
    main()
