# Desafioflex
## Objetivo
O desafio é criar uma API para o gerenciamento de tarefas utilizando o conceito de RESTFULL e deve conter, cadastro, listagem edição e deleção.

## Requisitos
Nossa stack é desenvolvida em Python 3, portanto o projeto deve ser realizado preferêncialmente em Django ou Flask
API deve seguir os princípios REST 
Salvar as informações necessárias em um dos bancos de dados relacionais abaixo:
- Sqlite
- PostgreSQL
- MySQL
Documentar com README como executar o projeto
Subir a aplicação em alguma plataforma (Exemplo Heroku)

## Diferencial
- Implementar utilizando Clean Architecture
- Utilizar SQLAlchemy na camada de banco
- Utilizar sql-migrate para construir banco
- Ter cobertura de teste no código (TDD - utilizando o pytest)

## Campos
```{
  "id": 1,
  "task": "Study", //obrigatório,
  "description": "",
  "created_at": "2020-10-21T13:45:11-03:00", //preenche com a data atual quando esta criando a atividade
  "updated_at": "2020-10-21T13:45:11-03:00" //preenche com a data atual quando esta modificando a atividade
} 
