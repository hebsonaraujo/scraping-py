import scrape_services.scrape as bla
from .config import data

instance = bla.Bs(data['url'],data["element"],data["selector"],data["action"])