from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

class Bs :
    def __init__(self, url, element, selector, func):
        self.url = url
        self.element = element
        self.selector = selector
        self.func = func

    def open_url(self,url = None):
        if url is None:
            url = self.url
        try:
            html = urlopen(url)
        except HTTPError:
            return None
        return html

    def get_html_from_url(self,url):
        return BeautifulSoup(self.open_url().read(),'html.parser')    

    def get_data(self):
        try:
            bsObj = BeautifulSoup(self.open_url().read(),'html.parser')
            els = bsObj.find_all(self.element,class_= self.selector)
            dados_exposicoes = []
            for el in els :
                title = el.find('h4', class_='titulo').text
                descr = el.find('p', class_='descricao-exposicao').text
                date = el.find('p', class_='data').text
                url = el.find('a', class_='btn').get('href')
                full_url = url if url.startswith("https://") else 'https://www.faap.br' + url
                link = BeautifulSoup(self.open_url(full_url).read(),'html.parser')
                text = link.find('div',class_='texto')
                if text:
                    fullText = [p.get_text() for p in text.find_all('p')]
                else:
                    print("Class 'texto' not found")
                dados_exposicoes.append({
                    "titulo": title,
                    "descricao": descr,
                    "data": date,
                    "url": full_url,
                    "text": fullText
                })
                self.save_json(dados_exposicoes,'dados_exposicoes')
        except HTTPError:
            return None
        return els

    def save_json(self,data_to_save,filename):
        with open(filename + '.json', 'w') as arquivo_json:
            json.dump(data_to_save, arquivo_json, indent=4)

    def init_scrapping(self):
        return self.get_data()
        
    def status(self):
        return 'acessando....' + self.url

