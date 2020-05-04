import mysql.connector
from mysql.connector import errorcode

#Faz a conexão com o DB
def conexaoSQL():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
  )
  return mydb

#Cria um noto database
#def criaDB(mydb):
#  mycursor = mydb.cursor()
#  mycursor.execute("CREATE DATABASE mydatabase")

#Cria cursor SQL
def criaCursor(dbUsado):
  cursorSQL = dbUsado.cursor()
  return cursorSQL

def listaDB(cursorUsado):
  cursorUsado.execute("SHOW DATABASES")

  lista = []
  for db in cursorUsado:
    lista.append(db)
  
  return lista

bancoDados = conexaoSQL()

cursorSQL = criaCursor(bancoDados)

listaDBS = listaDB(cursorSQL)

print(listaDBS)