#--------------------------------Explicito é melhor do que implicito-----------------------

queryInsert = "INSERT INTO tabela1 (COLUNA2, COLUNA3, COLUNA4) VALUES ('Outro Fido', '1994-06-09', 5)"

selectAll = "SELECT * FROM %s"

criaTabelaEntradas = "CREATE TABLE Entradas (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
"POSICAO_RANK INT(2), TITULO VARCHAR(100), ESTUDIO VARCHAR(100), ALTERACAO_RANK VARCHAR(10),"
"MOVIMENTACAO_RANK VARCHAR(3), POSICAO_MAIS_ALTA INT(2), POSICAO_ANTERIOR INTEGER(2),"
"SEMANAS_TOP INT(2) NULL, TEMPORADA VARCHAR(15), NUMERO_SEMANA INT(3), DATA_GRAFICO DATE)"

insertEntradas = "INSERT INTO Entradas(POSICAO_RANK, TITULO, ESTUDIO, ALTERACAO_RANK,"
"MOVIMENTACAO_RANK, POSICAO_MAIS_ALTA, POSICAO_ANTERIOR, SEMANAS_TOP, TEMPORADA, NUMERO_SEMANA,"
" DATA_GRAFICO) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

