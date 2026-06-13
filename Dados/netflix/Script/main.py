from fastapi import FastAPI, status,HTTPException
import uvicorn
from query import simple_find,seculo_passado,busca_ordenada,verificar_ator

app = FastAPI()

@app.get("/" ,tags=["GET"], status_code=status.HTTP_200_OK, summary="Rota padrão")
def padrao():
    return {"message": "Sucess"}

@app.get("/see_especific/{title}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie com busca por título")
def ver_especifico(title: str):
    res = simple_find(title)
    return {"Catalogo": res}

@app.get("/netflix_lt_2000",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie antes de 2000")
def abaixo_2000():
    res = seculo_passado()
    return {"Catalogo": res}

@app.get("/criminal_shows", tags=["GET"], status_code=status.HTTP_200_OK, summary="5 Criminals show ordenados descendente por title")
def desc_criminal():
    res = busca_ordenada()
    return {"Shows": res}

@app.get("/see_actor_especific/{name}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie que um ator esteve presente")
def ver_especifico(name: str):
    res = verificar_ator(name)
    if res == "Nome não encontrado em filmes ou series":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nome não encontrado em filmes ou series"
        )
    return {"Aparições": res}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)