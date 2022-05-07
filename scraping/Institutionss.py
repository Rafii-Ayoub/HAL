import urllib.request
import json
import ssl
import numpy as np
import matplotlib.pyplot as plt
import requests

ssl._create_default_https_context = ssl._create_unverified_context



#Get instituition ID

def institute_id(school_name):


    url = 'https://api.openalex.org/institutions?filter=display_name:'+ school_name 

    json_obj = urllib.request.urlopen(url)

    data = json.load(json_obj)

    item = data["results"]

    ID = item[0]["id"]
    if ID.startswith('https://openalex.org/'):
        return ID[len('https://openalex.org/'):]
    return ID, 


print(institute_id("Harvard%20University"))

def number_of_authors(institute_ID):

    url = 'https://api.openalex.org/authors?filter=last_known_institution.id:'+ institute_ID + '&per-page=200'

    json_obj = urllib.request.urlopen(url)

    data = json.load(json_obj)

    num_authors = data["meta"]["count"]
    
    return num_authors



def author_by_institute(institute_ID,author_num):

    url = 'https://api.openalex.org/authors?filter=last_known_institution.id:'+ institute_ID + '&per-page=200'
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    item = data["results"]
    ID = item[author_num]['id']
    if ID.startswith('https://openalex.org/'):
        return ID[len('https://openalex.org/'):]
    return ID
print(author_by_institute(institute_id("Harvard%20University"),50))


def author_cited_by(cited_by_api_url,items_per_page,author_ID,first_pub_year,year_range,first_pub_date):
    session = requests.Session()
    to_date = first_pub_year+year_range
    cited_by_url = cited_by_api_url+ '&filter=from_publication_date:'
    
    cited_by_url = cited_by_url + first_pub_date +',' + 'to_publication_date:' + str(to_date) +  '-01-01' + '&per-page=' + str(items_per_page)  
    params = {'mailto': 'jctanner@iu.edu'}
    session.headers.update(params)
    response = session.get(cited_by_url, headers=session.headers, params=params)
    assert response.status_code == 200, f'Response code: {response.status_code} '
    cited_by_data = response.json()
    cited_count = cited_by_data["meta"]["count"]
    session.close()

    return cited_count


def works_by_author(author_ID,years_from_first_pub,year_range):
    items_per_page = 200
    
    session = requests.Session()
    url = 'https://api.openalex.org/works?per-page=' + str(items_per_page) + '&sort=publication_year:asc' + '&cursor=*&filter=author.id:'+ author_ID + '&cursor=*'
  
    print("ok1")
    response = session.get(url, headers=session.headers)
    assert response.status_code == 200, f'Response code: {response.status_code} '
    data = response.json()
    item = data["results"]
    total_citations = 0
    
    if data["meta"]["count"] > 0:
  
        first_pub_date = item[0]['publication_date']
        first_pub_year = item[0]['publication_year']
        

        W = -1
        #Pass through pages of author work
        current_pub_year = 1 #initialize in order to start while loop
        while  current_pub_year <= first_pub_year + years_from_first_pub and data['meta']['next_cursor']:
            W +=1
          

            #update page
            next_cursor = data["meta"]["next_cursor"]

            url2 = 'https://api.openalex.org/works?per-page=' + str(items_per_page) + '&sort=publication_year:asc'+'&filter=author.id:'+ author_ID + '&cursor='
            url2 = url2 + next_cursor
            response = session.get(url2, headers=session.headers)
            assert response.status_code == 200, f'Response code: {response.status_code}'
            data = response.json()

            item = data["results"]
            print(item)
        

    session.close()    
    return total_citations


print(works_by_author("A1979847480",1900,100))