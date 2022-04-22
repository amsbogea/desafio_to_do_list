from crypt import methods

from pickle import GET

from flask import Flask,request

from main import insertTask

app = Flask("ItFlex")

#inicio da rota "/insert/task"
@app.route("/insert/task", methods=["POST"]) 
def xxxxxxxx():

    body = request.get_json()


    #INCIO -> testa se TODOS os paramentros estão devidamente imformados
    if("task" not in body):
        return {"status": 400, "mensagem": "o parametro 'task' é obrigatório!"}

    if("description" not in body):
        return {"status": 400, "mensagem": "o parametro 'description' é obrigatório!"}

    if("duration" not in body):
        return {"status": 400, "mensagem": "o parametro 'duration' é obrigatório!"}

    if("priority" not in body):
        return {"status": 400, "mensagem": "o parametro 'priority' é obrigatório!"}

    if("created_at" not in body):
        return {"status": 400, "mensagem": "o parametro 'created_at' é obrigatório!"}

    if("updated_at" not in body):
        return {"status": 400, "mensagem": "o parametro 'updated_at' é obrigatório!"}   

    #FINAL -> testa se TODOS os paramentros estão devidamente imformados                     

    task = insertTask(body["task"], body["description"], body["duration"], body["priority"], body["created_at"], body["updated_at"])

    return task
#fim da rota "/insert/task"  

app.run() #rodar a aplicação