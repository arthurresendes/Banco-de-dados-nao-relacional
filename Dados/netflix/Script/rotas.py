from fastapi import APIRouter, status,HTTPException, Request, Query
from query import simple_find,seculo_passado,busca_ordenada,verificar_ator,deletar,atualizar,adicionando_novo_objeto,tipos_de_filmes_series,paginacao
from Schemas import Atualizar,Adicionar
import string
from limitador import limiter
import math

router = APIRouter(prefix="/api/v1")

@router.get("/" ,methods=["GET", "HEAD"],tags=["GET"], status_code=status.HTTP_200_OK, summary="Rota padrão")
def padrao():
    return {"message": "Sucess"}

@router.get("/see_especific/{title}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie com busca por título")
def ver_especifico(title: str):
    title = string.capwords(title)
    res = simple_find(title)
    if res:
        if "_id" in res:
            res["_id"] = str(res["_id"])
        return res
        
    raise HTTPException(status_code=404, detail="Item não encontrado")

@router.get("/netflix_lt_2000",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie antes de 2000")
def abaixo_2000():
    res = seculo_passado()
    return {"Catalogo": res}

@router.get("/netflix_lt_2000_page",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie antes de 2000 com paginação")
def abaixo_2000_paginado(pagina: int = Query(1,ge=1)):
    limite = 20 
    pular = (pagina - 1) * limite
    res,total_pag = paginacao(pular,limite)
    pages_total = math.ceil(total_pag/limite)
    if pagina > pages_total:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Página sem documentos')
    return {"Catalogo": res, 'TotalPage': pages_total }


@router.get("/especifics_types/{type}", tags=["GET"], status_code=status.HTTP_200_OK, summary="5 shows de acordo com o tipo selecionado pelo user")
def desc_show(type: str):
    res = busca_ordenada(type)
    return {"Shows": res}

@router.get("/see_actor_especific/{name}",tags=["GET"], status_code=status.HTTP_200_OK, summary="Ver filme ou serie que um ator esteve presente")
def ver_especifico(name: str):
    name = string.capwords(name)
    res = verificar_ator(name)
    if res == "Nome não encontrado em filmes ou series":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nome não encontrado em filmes ou series"
        )
    return {"Aparições": res}

@router.get("/see_all_types", tags=["GET"], summary="Ver todos tipos de série/filmes que tem.", status_code=status.HTTP_200_OK)
def ver_tipos():
    todos_tipos = tipos_de_filmes_series()
    return {"Types": todos_tipos}

@router.post("/adicionando_novo", tags=["POST"], summary="Adicionando novo filme/série", status_code=status.HTTP_201_CREATED)
@limiter.limit('5/minute')
def adicionando_novo(request: Request,obj: Adicionar):
    res = adicionando_novo_objeto(obj.tipo,obj.nome,obj.ano,obj.raiting,obj.duration,obj.description,obj.cast,obj.paises,obj.directors,obj.listed)
    if res:
        return {'Mensagem': 'Cadastrado com sucesso', 'Objeto': obj}
    raise HTTPException(detail="Erro ao adicionar", status_code=status.HTTP_404_NOT_FOUND)

@router.patch("/atualizando" , tags=["PATCH"], summary="Adicionando ator ao cast", status_code=status.HTTP_202_ACCEPTED)
@limiter.limit('15/minute')
def atualizar_cast(request: Request,infos: Atualizar):
    nome = string.capwords(infos.nome)
    res = atualizar(nome, infos.ator)
    if res != "Atualizado":
        raise HTTPException(detail="Titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return {"Mensagem": f"{infos.ator} adicionado ao cast com sucesso"}

@router.delete("/delete_per_name/{name}", status_code=status.HTTP_204_NO_CONTENT, tags=["DELETE"], summary="Deletando por nome")
@limiter.limit('10/minute')
def deletando_por_nome(request: Request,name: str):
    name = string.capwords(name)
    res = deletar(name)
    if res != "Sucess":
        raise HTTPException(detail="Titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return None