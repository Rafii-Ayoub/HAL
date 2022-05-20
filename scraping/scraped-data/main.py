import json
import csv
"""with open("publications_info.json","r",encoding="utf8") as infile:
   with open("publications.json","w",encoding="utf8") as outfile:  
        publication_list =[]
        for row in json.loads(infile.read()):
            for publication in row["publications"]:  
                publication_dict = {}          
                publication_dict["title"] = publication["name"] 
                publication_dict["author"] = row["name"]
                publication_dict["link"] = publication["link"] 
                publication_dict["authorship"] = publication["authorship"] 
                publication_list.append(publication_dict)
        json.dump(publication_list, outfile,ensure_ascii=False)
        outfile.close()
        infile.close()"""
    
"""with open("keywords_info.json","r",encoding="utf8") as infile:
   with open("concepts.json","w",encoding="utf8") as outfile:  
        concepts_list =[]
        for row in json.loads(infile.read()):
            for publication in row["concepts"]:  
                publication_dict = {}          
                publication_dict["concepts"] = publication["concepts"] 
               
                concepts_list.append(publication_dict)
        json.dump(concepts_list, outfile,ensure_ascii=False)
        outfile.close()
        infile.close()"""

with open("keywords_info.json","r",encoding="utf8") as infile:
   with open("keywords_info_bis.json","w",encoding="utf8") as outfile:  
        list=[]
        for row in json.loads(infile.read()):
            if(len(row)>1):
              
                concepts_list = []
                
                for concept in row["concepts"]:  
                    concept = {"value":concept , "count":1}
                    concepts_list.append(concept)
                row["concepts"] = concepts_list
                list.append(row)     
                print(row)
        json.dump(list, outfile,ensure_ascii=False)
        outfile.close()
        infile.close()


   