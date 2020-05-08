#--------------------------------Explicito é melhor do que implicito-----------------------
#Lógica principal do scrap

from requestPagina import pegaPagina
from filtroHTML import analisaPagina, filtroCorpo, filtroCabecalho, encontraCabecalho
from filtroHTML import encontraClasse, extraiAtributos, encontraURLPaginacao
from time import sleep

import moduloSQL.funcoesSQL as funcoesSQL

def extraiInformacoes(url):
    #Request da pagina
    paginaCrua = pegaPagina(url)
    #Tratamento se a página não foi encontrada
    if paginaCrua == None:
        print("Pagina não encontrada")
        print(url)
        return None

    else:
        print("--------------------------------------------------")
        print("----------Iniciando Filtro----------")
        #Análise do HTML com a função que chama o bs4
        paginaAnalisada = analisaPagina(paginaCrua)
        print("Analisando pagina HTML...")

        #Função retorna um dicionario com as informações de temporada, data e número da semana
        dictCabecalho = filtroCabecalho(paginaAnalisada)
        print("Recuperando as informações do cabeçalho...")

        #Função que filtra o HTML para retornar uma lista de entradas do gráfico
        corpoGrafico = filtroCorpo(paginaAnalisada)
        #print("Lista possui %s entradas." % len(corpoGrafico))

        #For que filtra as informações de cada entrada e as coloca em um dicionario
        listaEntradas = extraiAtributos(corpoGrafico)
        print("Dicionario possui %s registros." % len(listaEntradas))

        #For que adiciona as informações do cabeçalho a cada uma das entradas da lista
        for entrada in listaEntradas:
            #print(entrada)
            entrada.update(dictCabecalho)
            #print(entrada)

        #print("Mostrando os 3 primeiros registros do dicionario")
        #for entrada in listaEntradas[0:3]:
        #    print(entrada, end='\n'*2)

        print("----------Encerrando Filtro----------")
        print("--------------------------------------------------", end= "\n"*2)
    return paginaAnalisada, listaEntradas

def raspaTodasPaginas(url):
    paginaAtual, listaEntradas = extraiInformacoes(urlInicial)
    linkPaginaAnterior = ""

    while linkPaginaAnterior != None:
        print("----------Informações da próxima página----------")
        linkPaginaAnterior = encontraURLPaginacao(encontraCabecalho(paginaAtual))
        print(linkPaginaAnterior)

        if linkPaginaAnterior == None :
            print("Não há mais páginas a serem acessadas")
            return(listaEntradas)
            
        else:
            print("----------")
            paginaAtual, novaListaEntradas = extraiInformacoes(linkPaginaAnterior)
            listaEntradas.extend(novaListaEntradas)
            print("Quantidade de registros na lista: %s" % len(listaEntradas))
            print("Esperando 30 segundos para solicitar a próxima pagina...")
            sleep(30)

urlInicial = "https://anitrendz.net/charts/top-anime/"
urlAnterior = "https://anitrendz.net/charts/top-anime/2014-01-31"

paginaAtual, listaEntradas = extraiInformacoes(urlInicial)
#listaTodas = raspaTodasPaginas(urlAnterior)


#SQL
#---------------Conexao SQL---------------
print("------------------------------------------------------------")
sqlConectado = funcoesSQL.conectaSQL() #Conecta ao MySQL
cursorSQL = funcoesSQL.criaCursor(sqlConectado) #Cria cursor

#----------------Usando DB-------------------
funcoesSQL.usaDB(cursorSQL, "ANITRENDZ") #Usa cursor para acessar banco de dados "teste"

#Insere informações na tabela Anitrendz
#funcoesSQL.insertTabela(cursor=cursorSQL, nomeTabela="entradas", 
#stringColunas= algumasColunas, valoresColunas = stringValores, lista=listaEntradas)

query = "INSERT INTO entradas (`POSICAO_RANK`, `TITULO`, `ESTUDIO`, `ALTERACAO_RANK`, `MOVIMENTACAO_RANK`, `POSICAO_MAIS_ALTA`, `POSICAO_ANTERIOR`, `SEMANAS_TOP`, `TEMPORADA`, `DATA_GRAFICO`, `NUMERO_SEMANA`) VALUES (%(Rank)s, %(Titulo)s, %(Estudio)s, %(Mudanca)s, %(Movimentacao)s, %(MaiorPosicao)s, %(PosicaoAnterior)s, %(SemanasTop)s, %(Temporada)s, %(DataGrafico)s, %(SemanaTemporada)s)"

cursorSQL.executemany(query, listaEntradas)
print("Inserindo informacoes na tabela")
print(cursorSQL.rowcount, "registros inseridos")


funcoesSQL.selectTudo(cursorSQL, "entradas")

sqlConectado.commit()
print("Commitando informacoes")

funcoesSQL.fechaCursor(cursorSQL)
funcoesSQL.desconectaSQL(sqlConectado)
print("Cursor e conexao fechados")

