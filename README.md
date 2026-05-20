# API de Gerenciamento de Tasks

Projeto desenvolvido em Python utilizando FastAPI para gerenciamento de tarefas através de uma API REST.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Deletar tarefas

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON

## Estrutura da Task

```json
{
  "tarefa": "Estudar FastAPI",
  "dataInicio": "2026-05-20",
  "dataFinal": "2026-05-25",
  "status": "Em andamento",
  "descricao": "Estudos sobre criação de APIs REST"
}
