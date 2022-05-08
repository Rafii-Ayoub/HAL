import urllib.request
import json
import ssl
import numpy as np
import matplotlib.pyplot as plt
from urllib.error import HTTPError

class institution:
    def __init__(self,institution_name):
        self.url = 'https://api.openalex.org/institutions?search=' + institution_name
        json_obj = urllib.request.urlopen(self.url)
        self.data= json.load(json_obj)
        self.institution_name = institution_name

    def get_institutions(self):
        institutions= []
        for item in self.data["results"]:
            institutions.append(item["display_name"])
        return self.data

    def get_id(self):

        url = 'https://api.openalex.org/institutions?filter=display_name:'+ self.institution_name
        json_obj = urllib.request.urlopen(url)
        data = json.load(json_obj)
        item = data["results"]
        if(len(item)>0):
            ID = item[0]["id"]
            if ID.startswith('https://openalex.org/'):
                return ID[len('https://openalex.org/'):]
            return ID,

    def get_authors_ids(self):
        url = 'https://api.openalex.org/works?filter=institution.id:'+ self.get_id()
        json_obj = urllib.request.urlopen(url)
        data = json.load(json_obj)
        L=[]
        for element in data["results"]:
            ID = element["id"]
            if ID.startswith('https://openalex.org/'):
                L.append(ID[len('https://openalex.org/'):])
        return L

    def get_authors_names(self):
        url = 'https://api.openalex.org/works?filter=institution.id:'+ self.get_id()
        json_obj = urllib.request.urlopen(url)
        data = json.load(json_obj)
        L=[]
        for element in data["results"]:
            ID = element["id"]
            if ID.startswith('https://openalex.org/'):
                id = ID[len('https://openalex.org/'):]
                url = 'https://api.openalex.org/authors/'+ id
                try:
                    json_obj = urllib.request.urlopen(url)
                    data = json.load(json_obj)
                    L.append(data["display_name"])
                except urllib.error.HTTPError as err:
                    pass
        return L        
        
  
        

print(institution("Universite%20Savoie%20Mont%20Blanc").get_authors_names())