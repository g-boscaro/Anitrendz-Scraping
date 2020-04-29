#Filtra usando o beautiful soup

#importa a lib
from bs4 import BeautifulSoup

#Usar classe e métodos?
def filtraPagina(pagina):
    paginaAnalisada = BeautifulSoup(pagina.content, 'html.parser')
    
    #Cabeçalho do Gráfico
    cabecalhoGrafico = paginaAnalisada.find('div', id="at-chart-top-header")
    
    #.strip() remove os espaços em branco da string
    temporada = cabecalhoGrafico.find('div', class_="at-cth-top-season").text.strip()
    dataGrafico = cabecalhoGrafico.find('div', class_="at-cth-b-date").text.strip()
    semanaTemporada = cabecalhoGrafico.find('div', class_="at-cth-b-week-no").text.strip()

    return temporada, dataGrafico, semanaTemporada