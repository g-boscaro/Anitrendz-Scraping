#Lógica principal do scrap

from requestPagina import pegaPagina
from filtroHTML import analisaPagina, filtroCabecalho, filtroCorpo

urlInicial = "https://anitrendz.net/charts/top-anime/"
#urlInicial = "https://anitrendz.net/zurb"

#Request da pagina
paginaCrua = pegaPagina(urlInicial)

if paginaCrua == None:
    exit()

else:
    #Parser HTMl
    paginaAnalisada = analisaPagina(paginaCrua)

    #Filtro cabeçalho
    temporada, data, semana = filtroCabecalho(paginaAnalisada)

    #print("Cabeçalho")
    #print("Temporada: %s \nData Chart: %s \nSemana: %s" % (temporada, data, semana))

    corpo = filtroCorpo(paginaAnalisada)


    #for entrada in corpo:

        #print(entrada, end='\n'*2)