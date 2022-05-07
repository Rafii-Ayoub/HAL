import urllib.request
import json
import ssl
import numpy as np
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context


class author:

    def __init__(self,author_name):
        self.url = 'https://api.openalex.org/authors?search=' + author_name
        json_obj = urllib.request.urlopen(self.url)
        self.data= json.load(json_obj)

    def get_authors(self):
        authors= []
        for item in self.data["results"]:
            authors.append(item["display_name"])
        return authors

    def get_last_known_institution(self):
        list = []
        if(len(self.data)==1):
            return self.data["results"]["last_known_institution"]
        elif(len(self.data)>1): 
            for item in self.data["results"]:
                if(item["last_known_institution"]):
                   l=[]
                   l.append(item["last_known_institution"]["display_name"])
                   l.append(item["last_known_institution"]["country_code"])
                list.append(l) 
            return list
        else:
            return None

    def key_words(self):
        list=[]
        for item in self.data["results"]:
            if(item["x_concepts"]):
                for element in item["x_concepts"]:
                       list.append(element["display_name"])

        return list

    def get_count_by_year(self):
        list=[]
        for item in self.data["results"]:
            if(item["counts_by_year"]):
                years=[] 
                works_count=[]
                cited_by_count=[]
                i=0
                dic ={}
                for element in item["counts_by_year"]:
                    years.append(element["year"])
                    i+=element["works_count"]
                    works_count.append(element["works_count"])
                    cited_by_count.append(element["cited_by_count"])  
                dic["autor_name"]=item["display_name"]    
                dic["years"]=years
                dic["works_count"]=works_count
                dic["cited_by_count"]=cited_by_count
                if(i>1):  
                    plt.plot(years,works_count)
                    plt.title(item["display_name"])
                    plt.show()
            else:
                return None

        return list

    def draw_count_by_year(self):

        for item in self.data["results"]:
            if(item["counts_by_year"]):
                years=[] 
                works_count=[]
                cited_by_count=[]
                i=0
                dic ={}
                for element in item["counts_by_year"]:
                    years.append(element["year"])
                    i+=element["works_count"]
                    works_count.append(element["works_count"])
                    cited_by_count.append(element["cited_by_count"])  
                if(i>3):  
                    plt.plot(years,works_count)
                    plt.title(item["display_name"])
                    plt.show()
            else:
                pass


with open('listic_members.txt', 'r') as f:
    #liste = f.split(";")
    l=f.read().split(";")

for k in l:
    k = k.replace(" ", "%20")
    s1 = author(str(k))
    print(s1.key_words())
        
