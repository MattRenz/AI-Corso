# Costruire un correttore ortografico

# date n parole calcola la matrice di distanza


def ChiediParole(inmParole):

    lSearch_List = []

    for i in range(inmParole):

        parola = input(f'Inserisci Parola {i}: ')
        lSearch_List.append(parola)

    return lSearch_List



from googleapiclient.discovery import build

# def google_search(api_key, query, num_results=10):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=query, cx='557a0cd6d60b549e5', num=num_results).execute()
    
#     items = res.get('items', [])
    
#     for item in items:
#         title = item['title']
#         link = item['link']
#         print(f'Title: {title}')
#         print(f'Link: {link}')
#         print('---')

# # Configura la tua chiave API e il numero di risultati desiderati
# api_key = 'AIzaSyCoDqu13VciBr3goGC0F3VligcV71wicfM'
# search_query = 'python tutorial'
# num_results = 5

# # Esegui la ricerca su Google
# google_search(api_key, search_query, num_results)

# ME

# from googleapiclient.discovery import build

# def google_search(api_key, query):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=query, cx='557a0cd6d60b549e5', num=1).execute()
    
#     total_results = res.get('searchInformation', {}).get('totalResults')
    
#     # print(f'Approximately {total_results} results')

#     return total_results

# # Configura la tua chiave API e la query di ricerca
# api_key = 'AIzaSyCoDqu13VciBr3goGC0F3VligcV71wicfM'
# search_query = 'cavallo'

# # Esegui la ricerca su Google
# print(google_search(api_key, search_query))

# 3.810.000

# 1) pip install google-api-python-client

# 2) Key Generator: https://developers.google.com/custom-search/v1/overview

# 3) YOUR_SEARCH_ENGINE_ID: https://programmablesearchengine.google.com/about/


# PROF

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def InitGoogleDriver():
    global driver
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')


def GetGoogleSearchResult(sStrToSearch):
    global driver
    driver.get("https://www.google.it/search?q=" + sStrToSearch)
    sAppo = driver.find_element("id","result-stats")
    print(sAppo.text)
    #return EstraiNumeroRisultati(sAppo.text)
    #search_bar = driver.find_element_by_name("q")
    #search_bar.clear()
    #search_bar.send_keys("getting started with python")
    #search_bar.send_keys(Keys.RETURN)
    #print(driver.current_url)

def EndGoogleDriver():
    global driver
    driver.close()




