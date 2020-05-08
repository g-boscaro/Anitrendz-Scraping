import funcoesSQL
import queriesSQL

#Conecta ao MySQL e cria o DB
conectaSQL = funcoesSQL.conectaSQL()
cursorSQL = funcoesSQL.criaCursor(conectaSQL)

#Cria DB Anitrendz
funcoesSQL.criaDB(cursorSQL, "ANITRENDZ")

#Usa DB anitrendz
funcoesSQL.usaDB(cursorSQL, "ANITRENDZ")

#Cria tabela entradas
cursorSQL.execute(queriesSQL.criaTabelaEntradas)
print("Tabela criada")

#Fecha cursor e sql
funcoesSQL.fechaCursor(cursorSQL)
funcoesSQL.desconectaSQL(conectaSQL)