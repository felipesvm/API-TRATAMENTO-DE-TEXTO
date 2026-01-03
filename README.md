<h1 align="center">📝 TextAPI — API de Tratamento de Texto</h1>

<p align="center">
  API REST desenvolvida com <strong>FastAPI</strong> para processamento e manipulação de textos,
  oferecendo funcionalidades como contagem de palavras, transformação de texto,
  substituição de termos e extração de informações.
</p>

<p align="center">
  🚀 Simples • ⚡ Rápida • 🧩 Ideal para estudos de APIs REST
</p>

---

## 🚀 Tecnologias Utilizadas

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-000000?style=flat&logo=gunicorn&logoColor=white" />
</p>

---

## 📖 Sobre o Projeto

A **TextAPI** é uma API desenvolvida com **FastAPI** que permite realizar diversos tipos de
tratamento e análise de textos por meio de endpoints simples e bem definidos.

O projeto tem como objetivo:

- Praticar a criação de **APIs REST**
- Trabalhar com **validação de dados** usando Pydantic
- Organizar endpoints de forma clara
- Servir como base para projetos maiores ou integrações futuras

---

## ✨ Funcionalidades Disponíveis

### 🔢 Análise de Texto

- Contagem de caracteres
- Contagem de palavras
- Contagem de frases
- Identificação da maior palavra e seu tamanho

### 🔄 Transformações

- Converter texto para maiúsculas
- Converter texto para minúsculas
- Capitalizar palavras
- Remover espaços extras
- Inverter texto
- Substituir palavras no texto

### 👤 Extração de Informações

- Extrair primeiro nome
- Extrair último nome

---

## 📌 Endpoints da API

| Método | Endpoint           | Descrição                             |
| ------ | ------------------ | ------------------------------------- |
| GET    | `/`                | Mensagem de boas-vindas               |
| POST   | `/contar`          | Conta caracteres, palavras e frases   |
| POST   | `/maiusculas`      | Converte texto para maiúsculas        |
| POST   | `/minusculas`      | Converte texto para minúsculas        |
| POST   | `/remover_espacos` | Remove espaços extras                 |
| POST   | `/inverter`        | Inverte o texto                       |
| POST   | `/substituir`      | Substitui palavras no texto           |
| POST   | `/primeiro_nome`   | Retorna o primeiro nome               |
| POST   | `/ultimo_nome`     | Retorna o último nome                 |
| POST   | `/tamanho_palavra` | Retorna a maior palavra e seu tamanho |
| POST   | `/capitalizar`     | Capitaliza todas as palavras          |

---

## 📦 Exemplo de Requisição

```json
{
  "texto": "João Silva Programador Python",
  "palavra_antiga": "Python",
  "palavra_nova": "FastAPI"
}
```
