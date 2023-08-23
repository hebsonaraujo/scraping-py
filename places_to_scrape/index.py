from .faap_museum.index import instance

list_sites = [instance]

for instance in list_sites:
    print(instance.status())
    if instance.init_scrapping() == None:
        print('value not be found')
    else:
        instance.init_scrapping()