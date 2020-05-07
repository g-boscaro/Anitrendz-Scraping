#--------------------------------Explicito é melhor do que implicito-----------------------
#Lógica principal do scrap

from requestPagina import pegaPagina
from filtroHTML import analisaPagina, filtroCorpo, filtroCabecalho
from filtroHTML import encontraCabecalho, encontraClasse, extraiAtributos, encontraURLPaginacao
from time import sleep

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

def raspaTodasPaginas(urlInicial):
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
            sleep(2)

urlInicial = "https://anitrendz.net/charts/top-anime/"
urlAnterior = "https://anitrendz.net/charts/top-anime/2014-01-31"
paginaAtual, listaEntradas = extraiInformacoes(urlInicial)

listaTodas = raspaTodasPaginas(urlAnterior)
print(listaTodas)
