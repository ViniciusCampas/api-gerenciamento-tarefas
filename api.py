import requests as rq

def imprimir(task):
    for tas in task:
        print(f'tarefa : {tas['tarefa']}')
        print(f'dataIniciua : {tas['dataIniciua']}')
        print(f'dataFinal : {tas['dataFinal']}')
        print(f'status : {tas['status']}')
        print(f'descricao : {tas['descricao']}')
        print('*'*100)

tasks = [
 
  {
    'tarefa': 'Revisar proposta comercial',
    'dataIniciua': '2026-05-28',
    'dataFinal': '2026-06-01',
    'status': 'pendente',
    'descricao': 'Verificar detalhes do orçamento e ajustar valores antes do envio final.'
  },
  {
    'tarefa': 'Organizar arquivos da equipe',
    'dataIniciua': '2026-06-02',
    'dataFinal': '2026-06-06',
    'status': 'pendente',
    'descricao': 'Separar documentos antigos e criar pastas novas no drive.'
  },
  {
    'tarefa': 'Responder e-mails pendentes',
    'dataIniciua': '2026-06-05',
    'dataFinal': '2026-06-05',
    'status': 'pendente',
    'descricao': 'Dar retorno aos clientes que aguardam resposta desde a última semana.'
  },
  {
    'tarefa': 'Atualizar planilha de despesas',
    'dataIniciua': '2026-06-08',
    'dataFinal': '2026-06-09',
    'status': 'pendente',
    'descricao': 'Adicionar gastos recentes e revisar totais.'
  },
  {
    'tarefa': 'Reunião com o setor de marketing',
    'dataIniciua': '2026-06-09',
    'dataFinal': '2026-06-12',
    'status': 'pendente',
    'descricao': 'Discutir próximos passos da campanha de fim de ano.'
  }
]

salvar=rq.post('http://127.0.0.1:8000/task/post',json=tasks)

consultar=rq.get('http://127.0.0.1:8000/task/get')

print ('PRIMEIRA CONSULTA')
print('='*100)
imprimir (consultar.json())
print('='*100)

tasksAlterada = {
    'tarefa': 'Revisar para refatorar o projeto',
    'dataIniciua': '2026-05-28',
    'dataFinal': '2026-06-01',
    'status': 'pendente',
    'descricao': 'Verificar o projeto para fazer sentido pra o cliente.'
  }

alterar=rq.put('http://127.0.0.1:8000/task/put/0',json=tasksAlterada)

consultar=rq.get('http://127.0.0.1:8000/task/get/id/0')
print ('CONSULTA DA ALTERAÇÃO')
print('='*100)
task =consultar.json()
print(f'tarefa : {task['tarefa']}')
print(f'dataIniciua : {task['dataIniciua']}')
print(f'dataFinal : {task['dataFinal']}')
print(f'status : {task['status']}')
print(f'descricao : {task['descricao']}')
print('='*100)

deletar =rq.delete('http://127.0.0.1:8000/task/delete/1')

consultar=rq.get('http://127.0.0.1:8000/task/get')

print ('CONSULTA DELETE')
print('='*100)
imprimir (consultar.json())
print('='*100)