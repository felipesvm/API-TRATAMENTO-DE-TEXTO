
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextoEntrada(BaseModel):

    texto: str
    palavra_antiga: str = None
    palavra_nova: str = None


@app.get("/")
def boas_vindas():


    return {"mensagem": "Bem-vindo(a) à API de Tratamento de Texto!"}



@app.post("/contar")
def contar_elementos(dados: TextoEntrada):

  
    texto = dados.texto

    numero_caracteres = len(texto)

    numero_palavras = len(texto.split())

    numero_frases = len([frase for frase in texto.split(".") if frase.strip() != ""])

   
    return {
        "numero_caracteres": numero_caracteres,
        "numero_palavras": numero_palavras,
        "numero_frases": numero_frases,
    }

@app.post("/maiusculas")
def converter_maiusculas(dados: TextoEntrada):
    return {"texto_maiusculas": dados.texto.upper()}

@app.post("/minusculas")
def converter_minusculas(dados: TextoEntrada):
    return {"texto_minusculas": dados.texto.lower()}
@app.post("/remover_espacos")
def remover_espacos(dados: TextoEntrada):
    return {"texto_sem_espacos": " ".join(dados.texto.split())}

@app.post("/inverter")
def inverter_texto(dados: TextoEntrada):
    return {"texto_invertido": dados.texto[::-1]}



@app.post("/substituir")
def substituir_texto(dados: TextoEntrada):
    if not dados.palavra_antiga or not dados.palavra_nova:
        return {"erro": "Por favor, forneça as palavras para substituição."}

    texto_modificado = dados.texto.replace(dados.palavra_antiga, dados.palavra_nova)

    return {"texto_modificado": texto_modificado}


@app.post("/primeiro_nome")
def extrair_primeiro_nome(dados: TextoEntrada):
    nomes = dados.texto.split()

    if nomes:
        return {"primeiro_nome": nomes[0]}
    return {"erro": "Texto vazio ou sem nome válido"}



@app.post("/ultimo_nome")
def extrair_ultimo_nome(dados: TextoEntrada):
    nomes = dados.texto.split()
    if nomes:
        return {"ultimo_nome": nomes[-1]}
    return {"erro": "Texto vazio ou sem nome válido"}



@app.post("/tamanho_palavra")
def calcular_tamanho_maior_palavra(dados: TextoEntrada):
    palavras = dados.texto.split()

    if palavras:

        maior_palavra = max(palavras, key=len)
        return {"maior_palavra": maior_palavra, "tamanho": len(maior_palavra)}

    return {"erro": "Texto vazio ou sem palavras"}

@app.post("/capitalizar")
def capitalizar_palavras(dados: TextoEntrada):
    return {"texto_capitalizado": dados.texto.title()}


