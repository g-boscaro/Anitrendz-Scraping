# Anitrendz-Scraping
Get Anitrendz charts info

Projeto pra extrair os dados do anitrendz
https://anitrendz.net/charts/top-anime/

Informações da página
--------------------------------------------------------------

Cabeçalho do chart
- Classe onde estão as informações de temporada, data e semana: class="current-page"
-- Temporada: Pegar o texto da class="at-cth-top-season"
-- Data do chart: Pegar o texto da class="at-cth-b-date"
-- Semana da temporada: Pegar o texto da class="at-cth-b-week-no"

Informações do chart
- Contem todas as entradas do chart: class="at-main-chart-entries"
Entrada do Chart
-- Contem cada entrada individual do chart: class="at-mcc-entry  "
--- Contem todas as informações da movimentação de cada entrada class="at-mcc-e-movement"
---- Contem a movimentação da entrada na semana: class="arrow-container"
----- Usar alt="Unchanged" para pegar o estado de movimentação
---- O número de movimentação da entrada: class="arrow-number"

---- Os status da entrada: class="stats"
----- A peak position: class="peak stats-entry  "
------ Número de peak position: <span></span>

----- A posição da semana anterior: class="prev stats-entry"
------ Número da posição da semana anterior: <span></span>

----- Semanas no top 10: class="weeks stats-entry"
------ Número de semanas no top 10: <span></span>

--- Contém o rank de uma entrada no texto: class="main-rank"

--- Contém o link da thumbnail, titulo, e estudio da entrada: class="at-mcc-e-details"
---- Thumbnail: class="at-mcc-e-thumbnail"
---- Título: class="entry-title"
---- Estudio: class="entry-detail"
---- Detalhes adicionais: class="entry-detail-3"

Paginação
- Classe do Botão da página anterior: class="at-cth-bottom"
-- Classe que contém o link da página anterior: class="prev-page"
--- Tag que contém o link da página anteior: <a href= ou através de alt="Previous Issue"

------------------------------------------------------------------

Lógica:
- Entrar na página: https://anitrendz.net/charts/top-anime/
- Pegar nome da temporada, data do chart, número da semana
- Pegar ranking, título, estudio, detalhes adicionais
- Pegar os status da entrada: peak position, posição da semana anterior, semanas no top 10

- Um loop pula para a próxima entrada se ela tiver a classe igual a class="at-mcc-entry  ", 
class="at-mcc-entry more-than-ten  unofficial-entry " ou class="at-mcc-entry more-than-ten " 
e pegar as mesmas informações anteriores, uma classe/método/função deve ser capaz de fazer isso

- Assim que o loop terminar, esperar 5 segundos, paginar para o chart anterior e pegar as informações
- Fazer isso até acabarem os charts

------------------------------------------------------
- O primeiro chart é de 19 de janeiro de 2014
- Há um gap de charts, de 29 dezembro de 2014 à 21 de janeiro de 2018 não há informações

Onde armazenar esta merda? SQL? Mongo? CSV? JSON?
