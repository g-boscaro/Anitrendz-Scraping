#Lógica principal do scrap
from pegaPagina import pegaPagina
from filtroHTML import filtraPagina

urlInicial = "https://anitrendz.net/charts/top-anime/"

#Request da pagina
paginaCrua = pegaPagina(urlInicial)

temporada, data, semana = filtraPagina(paginaCrua)

print("Temporada: %s \nData Chart: %s  " % (temporada, data))
print("Semana: " % semana)