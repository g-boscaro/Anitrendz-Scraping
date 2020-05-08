import funcoesSQL
import queriesSQL

#---------------Conexao SQL---------------
sqlConectado = funcoesSQL.conectaSQL() #Conecta ao MySQL
cursorSQL = funcoesSQL.criaCursor(sqlConectado) #Cria cursor
#listaBancos = funcoesSQL.listaDB(cursorSQL) #Cria lista de bancos de dados
#print(listaBancos)

#----------------Usando DB-------------------
funcoesSQL.usaDB(cursorSQL, "teste") #Usa cursor para acessar banco de dados "teste"
#listaTables = funcoesSQL.listaTabelas(cursorSQL) #Lista tabelas no banco de dados acessado
#print(listaTables)

#----------------INSERT-------------------
#queryInsert = queriesSQL.queryInsert
#cursorSQL.execute(queryInsert)
#print(cursorSQL.rowcount, "registros inseridos")

#----------------SELECT-------------------
funcoesSQL.selectTudo(cursorSQL,"tabela1")

#----------------COMMIT------------------------
#sqlConectado.commit()
#print("Commitando as informações para a tabela")

#------------Fechando Conexões----------------
funcoesSQL.fechaCursor(cursorSQL)
funcoesSQL.desconectaSQL(sqlConectado)