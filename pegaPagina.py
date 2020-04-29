#Faz o request das páginas
import requests

#Cabeçalho que é usado no request para simular um navegador
headers = {'User-Agent': 'Mozilla/5.0'}

def pegaPagina(url):
    pagina = requests.get(url, headers=headers, timeout= 5.001)
    print("Status code: %s" % pagina.status_code)
    print("URL da Pagina: %s" % pagina.headers["Location"])
    print("Tipo conteúdo: %s" % pagina.headers['content-type'])
    #print("Redirecionamentos: %s" % pagina.history)

    return pagina