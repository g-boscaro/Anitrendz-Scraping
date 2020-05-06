import queriesSQL
import mysql.connector
from mysql.connector import errorcode

#Faz a conexão com o MYSQL
def conectaSQL():
  try:
    conexaoSQL = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="1234"
    )
    print("Conexão com SQL feita!")
    return conexaoSQL

  except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database nao existe")
    
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Usuario ou senha incorretos")
    
    else:
      print(error)
    
  else:
    conexaoSQL.close()
    print("Conexao com SQL encerrada")

def desconectaSQL(conexaoSQL):
  conexaoSQL.close() #Desconecta do mysql
  print("Desconectado do MySQL")

#Cria cursor SQL
def criaCursor(conexaoSQL):
  cursorSQL = conexaoSQL.cursor()
  print("Criando cursor: %s" % cursorSQL)
  return cursorSQL
#Fecha cursor
def fechaCursor(cursorCriado):
  cursorCriado.close()
  print("Fechando o cursor: %s" % cursorCriado)

#Cria um noto database
def criaDB(cursorUsado, nomeDatabase):
  cursorUsado.execute("CREATE DATABASE IF NOT EXISTS %s" % nomeDatabase)
  print("Criado database: %s" % nomeDatabase)

#Conecta ao DB selecionado
def usaDB(cursorUsado, dbConectado):
  try:
    cursorUsado.execute("USE %s" % dbConectado)
    print("Conectado ao DB: %s" % dbConectado)
  
  except mysql.connector.Error as error:
      if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database nao existe")
      
      else:
        print(error)

#Lista os banco de dados do servidor
def listaDB(cursorUsado):
  cursorUsado.execute("SHOW DATABASES")

  lista = []
  for db in cursorUsado:
    lista.append(db)
  
  return lista

#Lista tabelas
def listaTabelas(cursorUsado):
  cursorUsado.execute("SHOW TABLES")
  tabelas = []
  for tabela in cursorUsado:
    tabelas.append(tabela)
  return tabelas

#Funcao SELECT *
def selectTudo(cursor, nomeTabela):
  querySelect = queriesSQL.selectAll %(nomeTabela)
  #querySelect = ("SELECT coluna2, coluna3 FROM tabela1")
  cursor.execute(querySelect)

  resultadoQuery = cursor.fetchall()

  for elemento in resultadoQuery:
    print(elemento)
  print()



#---------------Conexao SQL---------------
sqlConectado = conectaSQL() #Conecta ao MySQL
cursorSQL = criaCursor(sqlConectado) #Cria cursor
#listaBancos = listaDB(cursorSQL) #Cria lista de bancos de dados
#print(listaBancos)

#----------------Usando DB-------------------
usaDB(cursorSQL, "teste") #Usa cursor para acessar banco de dados "teste"
#listaTables = listaTabelas(cursorSQL) #Lista tabelas no banco de dados acessado
#print(listaTables)

#----------------INSERT-------------------

#queryInsert = queriesSQL.queryInsert
#cursorSQL.execute(queryInsert)
#print(cursorSQL.rowcount, "registros inseridos")

#----------------SELECT-------------------
selectTudo(cursorSQL,"tabela1")

#----------------COMMIT------------------------
#sqlConectado.commit()
#pritn("Commitando as informações para a tabela")

#------------Fechando Conexões----------------
fechaCursor(cursorSQL)
desconectaSQL(sqlConectado)