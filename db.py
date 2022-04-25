from click import password_option
from flask import Flask
import mysql.connector

con = mysql.connector.conect(host='localhost', database='TODOLIST', user='alex', password='Alexela')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ap servidor Mysql versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)
    

if con.is_connected():
    cursor.close()    
    con.close()
    print("Conexão ao MySQL foi encerrada")