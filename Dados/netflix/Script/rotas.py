from fastapi import APIRouter, status,HTTPException
from query import simple_find,seculo_passado,busca_ordenada,verificar_ator,deletar,atualizar
from Schemas import Atualizar

router = APIRouter(prefix="/api/v1")

@router.get("/" ,tags=["GET"], status_code=status.HTTP_200_OK, summary="Rota padrão")
def padrao():
    return {"message": "Sucess"}

@router.get("/see_especific/{title}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie com busca por título")
def ver_especifico(title: str):
    res = simple_find(title)
    return {"Catalogo": res}

@router.get("/netflix_lt_2000",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie antes de 2000")
def abaixo_2000():
    res = seculo_passado()
    return {"Catalogo": res}

@router.get("/criminal_shows", tags=["GET"], status_code=status.HTTP_200_OK, summary="5 Criminals show ordenados descendente por title")
def desc_criminal():
    res = busca_ordenada()
    return {"Shows": res}

@router.get("/see_actor_especific/{name}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie que um ator esteve presente")
def ver_especifico(name: str):
    res = verificar_ator(name)
    if res == "Nome não encontrado em filmes ou series":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nome não encontrado em filmes ou series"
        )
    return {"Aparições": res}

@router.patch("/atualizando" , tags=["PATCH"], summary="Adicionando ator ao cast", status_code=status.HTTP_202_ACCEPTED)
def atualizar_cast(infos: Atualizar):
    res = atualizar(infos.nome, infos.ator)
    if res != "Atualizado":
        raise HTTPException(detail="Titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return {"Mensagem": f"{infos.ator} adicionado ao cast com sucesso"}

@router.delete("/delete_per_name", status_code=status.HTTP_204_NO_CONTENT, tags=["DELETE"], summary="Deletando por nome")
def deletando_por_nome(nome: str):
    res = deletar(nome)
    if res != "Sucess":
        raise HTTPException(detail="Titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return {"Mensagem": f"{nome} Deletado com sucesso"}
