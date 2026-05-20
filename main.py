import json
from pydantic import BaseModel
from fastapi import FastAPI
#Foi instalado o Uvicorn para rodar o servidor na porta http://localhost:8000
#uvicorn main:app --reload 

class Task(BaseModel):
    tarefa: str
    dataIniciua:str
    dataFinal: str
    status:str
    descricao: str

app=FastAPI()

def salvarTasks(tasksList,CAMINHO_ARQUIVO):
     with open(CAMINHO_ARQUIVO,'w',encoding='utf-8') as arquivo:
         json.dump(tasksList,arquivo,indent=2,ensure_ascii=False)
      
def carregarTasks(CAMINHO_ARQUIVO):
    lista=[]
    try:
        with open(CAMINHO_ARQUIVO,'r',encoding='utf-8') as arquivo:
            lista= json.load(arquivo)
            return lista
     
    except FileNotFoundError:
        print('Arquivo nao encontrado')
        salvarTasks([],CAMINHO_ARQUIVO)
        return []

CAMINHO_ARQUIVO='task.json'

tasksList=carregarTasks(CAMINHO_ARQUIVO)

@app.get('/task/get')
def metodoGet():
    return tasksList

@app.get('/task/get/id/{task_id}')
def metodoGet(task_id:int):
    return tasksList[task_id]

@app.post('/task/post')
def metodoPost(tasks:list[Task]):
    for task in tasks:
        tasksList.append(task.model_dump())
    salvarTasks(tasksList,CAMINHO_ARQUIVO)
    return {'message':'Task(s) Criada(s)'}

@app.put('/task/put/{task_id}')
def metodoPut(task_id:int,tasks:Task):
    tasksList[task_id] = tasks.model_dump()
    salvarTasks(tasksList,CAMINHO_ARQUIVO)
    return {'message':'Task alterada','id':task_id}

@app.delete('/task/delete/{task_id}')
def metodoDelete(task_id:int):
    del tasksList[task_id]
    salvarTasks(tasksList,CAMINHO_ARQUIVO)
    return {'message':'Task deletada','id':task_id}
