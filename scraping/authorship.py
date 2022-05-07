import urllib.request
import json
import ssl
import numpy as np
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context



date_range = '2000-2004'
type = 'search=Salamatian%20Kave' 
url = 'https://api.openalex.org/authors?'+type
json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)
print(data)


def get_num_authors(data):

    num_authors = np.zeros(len(data["results"]))
    for item in data["results"]:
        print(item["display_name"])

    return num_authors


def get_last_known_institution(data):
   
    num_authors = np.zeros(len(data["results"]))
    for item in data["results"]:
        if(item["last_known_institution"]):
            print(item["last_known_institution"]["display_name"])
            print(item["last_known_institution"]["country_code"])
        else:
            print("None")

    return num_authors

def key_words(data):
    num_authors = np.zeros(len(data["results"]))
    for item in data["results"]:
        if(item["x_concepts"]):
            for element in item["x_concepts"]:
                print(element["display_name"])
            
        else:
            print("None")

    return num_authors



def work_counts(data):
   
    num_authors = np.zeros(len(data["results"]))
    for item in data["results"]:
        print(item["works_count"])

    return num_authors

def get_count_by_year(data):
    num_authors = np.zeros(len(data["results"]))
    for item in data["results"]:
        if(item["counts_by_year"]):
            years=[] 
            works_count=[]
            cited_by_count=[]
            i=0
            for element in item["counts_by_year"]:
                years.append(element["year"])
                i+=element["works_count"]
                works_count.append(element["works_count"])
                cited_by_count.append(element["cited_by_count"])   
            if(i>1):  
               plt.plot(years,works_count)
               plt.title(item["display_name"])
               plt.show()
        else:
            print("None")

    return num_authors

get_count_by_year(data)