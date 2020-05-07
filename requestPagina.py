#Faz o request das páginas
import requests

#Cabeçalho que é usado no request para simular um navegador
headers = {'User-Agent': 'Mozilla/5.0'}

def pegaPagina(url):
    try:
        print("----------Iniciando Request----------")
        print("Pegando pagina: %s" % url)
        pagina = requests.get(url, headers=headers, timeout= 10.001)
        paginaStatusCode = pagina.status_code
        
    except requests.HTTPError:
        print("Erro HTTP")
        return None

    if paginaStatusCode == 404 and '404 Not Found' in pagina.text:
        return None

    else:
        print("Status code: %s" % paginaStatusCode)
        #print("URL da Pagina: %s" % pagina.headers["Location"])
        print("Tipo conteúdo: %s" % pagina.headers['content-type'])
        print("----------Encerrando Request----------", end="\n"*2)
        return pagina