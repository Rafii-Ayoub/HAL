import json
from difflib import SequenceMatcher


with open("publications_info.json",mode = "r",encoding="utf8") as file:
    l = file.read()
    results = json.loads(l)
    liste1=[]
    for k in range(len(results)):
       
        
        if(len(results[k])>0):
        
            result = results[k]
            for element in result["publications"]:
                description = ""
                for author in element["authorship"]:
                    description += author+", "
                description = description +" " + element["name"]
                liste1.append(description)

            

   
        

with open("scraping/test.json",mode = "r",encoding="utf8") as file:
    l = file.readlines()[0]
    result = json.loads(l)["Result"]
    liste2= []
    for k in range(0,len(result)):
        liste2.append(result[k]["label_s"]) 
       
  


liste3=[]
liste4=[]
with open("articles_to_insert.txt", "w") as file:
    for a in liste1: 
        print(a)
        for b in liste2:
            ratio = SequenceMatcher(None, a, b).ratio()
            if ratio>0.5:
                liste4.append([a,b])
            else:
                if not(a in liste3):
                   liste3.append(a)
    file.write(str(liste3))  
    

    