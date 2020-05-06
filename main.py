#--------------------------------Explicito é melhor do que implicito-----------------------
#Lógica principal do scrap

from requestPagina import pegaPagina
from filtroHTML import analisaPagina, filtroCorpo, filtroCabecalho, encontraCabecalho, encontraClasse, loopEntradas

urlInicial = "https://anitrendz.net/charts/top-anime/"

#Request da pagina
paginaCrua = pegaPagina(urlInicial)

#Tratamento se a página não foi encontrada
if paginaCrua == None:
    exit()

else:
    #Análise do HTML com a função que chama o bs4
    paginaAnalisada = analisaPagina(paginaCrua)
    print("Analisando pagina HTML...")

    #Função retorna um dicionario com as informações de temporada, data e número da semana
    dictCabecalho = filtroCabecalho(paginaAnalisada)
    print("Recuperando as informações do cabeçalho...")

    #Função que filtra o HTML para retornar uma lista de entradas do gráfico
    corpoGrafico = filtroCorpo(paginaAnalisada)
    print("Lista possui %s entradas." % len(corpoGrafico))

    #For que filtra as informações de cada entrada e as coloca em um dicionario
    listaEntradas = loopEntradas(corpoGrafico)
    print("Dicionario possui %s registros." % len(listaEntradas))

    #For que adiciona as informações do cabeçalho a cada uma das entradas da lista
    for entrada in listaEntradas:
        #print(entrada)
        entrada.update(dictCabecalho)
        #print(entrada)
    
    #print(listaEntradas[10:13], end='\n'*2)

    #for entrada in corpo:

        #print(entrada, end='\n'*2)