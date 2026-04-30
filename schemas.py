from pydantic import BaseModel
from typing import Optional

# Entrada de dados (O que o usuário envia)
class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None

# Saída de dados (O que a API retorna)
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

    class Config:
        from_attributes = True # Permite ler objetos do SQLAlchemy[cite: 5]