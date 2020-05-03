#Lógica principal do scrap

from requestPagina import pegaPagina
from filtroHTML import analisaPagina, filtroCorpo, encontraCabecalho, encontraClasse, loopEntradas

urlInicial = "https://anitrendz.net/charts/top-anime/"
#urlInicial = "https://anitrendz.net/zurb"

#Request da pagina
paginaCrua = pegaPagina(urlInicial)

#Tratamento se a página não foi encontrada
if paginaCrua == None:
    exit()

else:
    #Análise HTMl com a função que chama o bs4
    paginaAnalisada = analisaPagina(paginaCrua)

    #Filtro cabeçalho
    #temporada, data, semana = filtroCabecalho(paginaAnalisada)
    cabecalho = encontraCabecalho(paginaAnalisada)
    temporada = encontraClasse(cabecalho, 'div', "at-cth-top-season")
    dataGrafico = encontraClasse(cabecalho, 'div', "at-cth-b-date")
    semanaTemporada = encontraClasse(cabecalho, 'div', "at-cth-b-week-no")



    corpoGrafico = filtroCorpo(paginaAnalisada)

    listaEntradas = loopEntradas(corpoGrafico)

    print(listaEntradas)

    #for entrada in corpo:

        #print(entrada, end='\n'*2)