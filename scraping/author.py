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
        print(self.data)
        return authors
    
    def get_authors_info(self):
        authors= []
        for item in self.data["results"]:
            dict = {}
            dict["name"] = item["display_name"]
            if(len(item)>0):
                ID = item["id"]
                if ID.startswith('https://openalex.org/'):
                    dict["id"] = ID[len('https://openalex.org/'):]
            elif(len(item)==0):
                dict["id"]={}

            if(item["last_known_institution"]):
                   l={}
                   l["name"]=item["last_known_institution"]["display_name"]
                   l["country"]=item["last_known_institution"]["country_code"]
                   dict["institution"] = l
            elif(not(item["last_known_institution"])):
                dict["institution"]={}

            if(item["x_concepts"]):
                list=[]
                for element in item["x_concepts"]:
                       list.append(element["display_name"])
                dict["concepts"] = list

            elif(not(item["x_concepts"])):
                dict["concepts"]={}

            authors.append(dict)
                
        return authors

    def get_publications(self):
        pub_list=[]
        for item in self.data["results"]:
            pub_dict = {}
            if(len(item)>0):
                ID = item["id"]
                if ID.startswith('https://openalex.org/'):
                    ID = ID[len('https://openalex.org/'):]
                pub_dict["id"]=ID 
                pub_dict["name"]=item["display_name"]     
                url = "https://api.openalex.org/works?filter=author.id:"+ID
                print(url)
                json_obj = urllib.request.urlopen(url)
                data2 = json.load(json_obj)
                list2 =[]
                for item in data2["results"]:
                    dict2={}
                    dict2["name"]= item["display_name"]
                    dict2["link"] = item["doi"]
                    l=[]
                    for author in item["authorships"]:
                        if (author["author"]["display_name"]):
                            l.append(author["author"]["display_name"])
                    dict2["authorship"]=l
                    list2.append(dict2)
                pub_dict["publications"] = list2
            pub_list.append(pub_dict)

        return pub_list
    
    def get_publications(self):
        pub_list=[]
        for item in self.data["results"]:
            pub_dict = {}
            if(len(item)>0):
                ID = item["id"]
                if ID.startswith('https://openalex.org/'):
                    ID = ID[len('https://openalex.org/'):]
                pub_dict["id"]=ID 
                pub_dict["name"]=item["display_name"]     
                url = "https://api.openalex.org/works?filter=author.id:"+ID
                print(url)
                json_obj = urllib.request.urlopen(url)
                data2 = json.load(json_obj)
                list2 =[]
                for item in data2["results"]:
                    dict2={}
                    dict2["name"]= item["display_name"]
                    dict2["link"] = item["doi"]
                    l=[]
                    for author in item["authorships"]:
                        if (author["author"]["display_name"]):
                            l.append(author["author"]["display_name"])
                    dict2["authorship"]=l
                    list2.append(dict2)
                pub_dict["publications"] = list2
            pub_list.append(pub_dict)

        return pub_list
   

    def get_authorship(self):

        authors_list=[]
        pub_dict = {}
        for item in self.data["results"]:
            
            pub_dict["author"]=item["display_name"]
            if(len(item)>0):
                ID = item["id"]
                if ID.startswith('https://openalex.org/'):
                    ID = ID[len('https://openalex.org/'):]    
                url = "https://api.openalex.org/works?filter=author.id:"+ID

                json_obj = urllib.request.urlopen(url)
                data2 = json.load(json_obj)
                
               
                for item in data2["results"]:
                    for author in item["authorships"]:
                        if (author["author"]["display_name"]):
                            authors_list.append(author["author"]["display_name"])    

        res={}
        for i in authors_list:
            res[i] = authors_list.count(i)
        pub_dict["Coauthors"] = res
        return pub_dict
   

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

    def get_authors_publications(self):
        authors= []
        for item in self.data["results"]:
            dict = {}
            dict["name"] = item["display_name"]
            if(len(item)>0):
                ID = item["id"]
                if ID.startswith('https://openalex.org/'):
                    dict["id"] = ID[len('https://openalex.org/'):]

    def key_words(self):
        list=[]
        for item in self.data["results"]:
            if(item["x_concepts"]):
                for element in item["x_concepts"]:
                       list.append(element["display_name"])

       
        return list
    
    def work_counts(self):
        i=0
        works_dict={}
        for item in self.data["results"]:
            i += item["works_count"]
            works_dict["name"] = item["display_name"] 
        works_dict["works_count"] = i
        return works_dict

    def get_count_by_year(self):
        list=[]
        for item in self.data["results"]:
            
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



with open('scraping/names.txt', 'r') as f:
    #liste = f.split(";")
    listic_members=f.read().split("\n")
 

"""dict ={}
l=[]
for k in listic_members:
        k = k.replace(" ", "%20")
        s1 = author(str(k))
        print("ok1")
        l.append(s1.get_publications())
        print(l)
with open('publications_info.json', 'w') as jsonFile:
    dict["result"] =l   
    json.dump(dict, jsonFile)
    jsonFile.close()
        """
        
"""l=[]
for k in listic_members:
        k = k.replace(" ", "%20")
        s1 = author(str(k))
        print("ok"+str(k))
        l+= s1.key_words()
        keywords=[]
        for i in l:
          count =l.count(i)
          if(count>100):
            keyword_dic={}
            keyword_dic["value"] = i
            keyword_dic["count"] = count
            keywords.append(keyword_dic)
        
       

with open('keyword_bis.json', 'w', encoding='utf-8') as jsonFile: 
    json.dump(keywords, jsonFile,ensure_ascii=False)
    jsonFile.close()"""


l=[]
for k in listic_members:
        k = k.replace(" ", "%20")
        s1 = author(str(k))
        print("ok"+str(k))
        l.append(s1.work_counts())
with open('statistics.json', 'w', encoding='utf-8') as jsonFile: 
    json.dump(l, jsonFile,ensure_ascii=False)
    jsonFile.close()
