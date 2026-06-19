from pydantic import BaseModel,Field
from typing import List

class Atualizar(BaseModel):
    nome: str
    ator: str

class Adicionar(BaseModel):
    tipo: str
    nome: str
    ano: int
    raiting: str
    duration: str
    description: str
    cast: List[str]
    paises: List[str]
    directors: List[str]
    listed: List[str]