# Gerador de Certificados

Este projeto gera automaticamente certificados personalizados para estudantes com mais de 70% de presença em eventos cadastrados no banco MySQL. Feito especificamente para o evento SECOMP UFSCar.

Ele usa Python + Pillow + dotenv, e preenche automaticamente os nomes dos alunos sobre um modelo de certificado em PNG.

<br>

## 📜 Pré-requisitos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

<br>

Por ter sido desenvolvido especificamente para o evento SECOMP UFSCar, este gerador de certificados foi projetado para funcionar com a estrutura de banco de dados utilizada nesse evento.

Para garantir o correto funcionamento, é necessário que o banco de dados contenha pelo menos as seguintes tabelas:
- users
- userAtActivity
- atividades

<br>

Além disso, adicione o modelo de certificado (em formato .png) na pasta assets/, com o nome **modelo_certificado.png**.

Será preciso ajustar as coordenadas de posicionamento do nome dos participantes, de acordo com o layout do seu modelo.

<br>

> 💡 **Dica:** Você pode adaptar o código facilmente para o seu próprio contexto, ajustando o nome das tabelas, colunas ou a estrutura do banco de dados conforme necessário.

<br>

## ⚙️ Setup

Clone o repositório:
```
https://github.com/enzomurayama/certificate-generator.git
cd certificate-generator
```

<br>

Instale as dependências:
```
pip install -r requirements.txt
```

<br>

Crie seu arquivo .env a partir do exemplo:
```
cp .env.example .env
```

<br>

Por fim, edite o .env com suas configurações reais.

<br>

## 💻 Uso

Execute o script principal:
```
python -m src.main
```
