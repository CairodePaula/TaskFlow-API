from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import get_db

app = FastAPI(title="Gerenciador de Tarefas")

# Criar Tarefa
@app.post("/tarefas/", response_model=schemas.TarefaResponse)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    nova_tarefa = models.Tarefa(**tarefa.model_dump())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

# Listar todas
@app.get("/tarefas/", response_model=List[schemas.TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(models.Tarefa).all()

# Buscar por ID
@app.get("/tarefas/{tarefa_id}", response_model=schemas.TarefaResponse)
def obter_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

# Deletar
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    return {"status": "removido com sucesso"}