#Filtra usando o beautiful soup

#importa a lib
from bs4 import BeautifulSoup

def analisaPagina(pagina):
    paginaAnalisada = BeautifulSoup(pagina.content, 'html.parser')
    return paginaAnalisada

#Encontra o Cabeçalho do Gráfico utilizando o id
def encontraCabecalho(paginaAnalisada):
    cabecalhoGrafico = paginaAnalisada.find('div', id="at-chart-top-header")
    return cabecalhoGrafico

#Encontra o texto dentro da classe html na página e retira os espaços em branco no começo e no fim da string
def encontraClasse(paginaAnalisada, taghtml, classehtml):
    return paginaAnalisada.find(taghtml, class_=classehtml).text.strip()

#def filtroCabecalho(paginaAnalisada):
#    #.strip() remove os espaços em branco da string
#    temporada = paginaAnalisada.find('div', class_="at-cth-top-season").text.strip()
#    dataGrafico = cabecalhoGrafico.find('div', class_="at-cth-b-date").text.strip()
#    semanaTemporada = cabecalhoGrafico.find('div', class_="at-cth-b-week-no").text.strip()
#    return temporada, dataGrafico, semanaTemporada

def filtroCorpo(paginaAnalisada):
    #Corpo do gráfico
    corpoGrafico = paginaAnalisada.find('div', class_="at-main-chart-entries")
    #find_all retorna uma lista que contém todas as tags das entradas do gráfico
    entradaGrafico = corpoGrafico.find_all('div', class_="at-mcc-entry")
    return entradaGrafico

def loopEntradas(entradaGrafico):    
    for entrada in entradaGrafico:
        #Detalhes Entrada
        tituloEntrada = entrada.find('div', class_="entry-title").text.strip()
        estudioEntrada = entrada.find('div', class_="entry-detail").text.strip()

        #Movimentação Entrada
        arrowEntrada = entrada.find('div', class_="arrow-container")
        statusMovimentacao = arrowEntrada.find('img')['alt']
        
        numeroMovimentacao = entrada.find('div', class_="arrow-number").text.strip()

        #Status Entrada
        statusEntrada = entrada.find('div', class_="stats")
        posicaoMaisAlta = statusEntrada.find('div', class_="peak stats-entry").text.strip()
        posicaoAnterior = statusEntrada.find('div', class_="prev stats-entry").text.strip()
        semanasTop = statusEntrada.find('div', class_="weeks stats-entry").text.strip()

        posicaoRank = entrada.find('div', class_="at-mcc-e-rank").text.strip()

    return entradaGrafico