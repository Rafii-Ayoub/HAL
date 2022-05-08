import requests 
import json
class HAL:

    def __init__(self):
        self.HALPapers={"Result":[]}
        self.HALPapersIds=[]
        json.dumps(self.HALPapers)
    #using the HAL API to get the articals where the name and the last name of the resercher exists
    def getPaperByName(self,name,lastname):
        response = requests.get('https://api.archives-ouvertes.fr/search/?q=({} {})'.format(name,lastname)).json()
        for i in response["response"]["docs"]:
            self.HALPapers["Result"].append(i)
            self.HALPapersIds.append(i["docid"])
            print(i)

    def getHALRegistredPapers(self):
        researchers = open('names.txt','r')
        names=researchers.readlines()
        for name in names:
            hal.getPaperByName(name.split()[0],name.split()[1])
        with open('test.json', 'w') as jsonFile:
            print(self.HALPapers)
            #self.removeDuplicates()
            json.dump(self.HALPapers, jsonFile)
            jsonFile.close()
        print(self.HALPapersIds)

    def removeDuplicates(self):
        indexItemsToRemove=[]
        for i in range(0, len(self.HALPapersIds)):  
            for j in range(i+1, len(self.HALPapersIds)):  
                if(self.HALPapersIds[i] == self.HALPapersIds[j]):  
                    indexItemsToRemove.append(j)
        print(self.HALPapersIds)
        print(indexItemsToRemove)
        for i in indexItemsToRemove:
            try:
                self.HALPapersIds.remove(self.HALPapersIds[i])
                self.HALPapers["Result"].remove(self.HALPapersIds[i])
            except :
                pass
        print(self.HALPapersIds)

    def setHALPapersIds(self,data):
        self.HALPapersIds=data

hal = HAL()
hal.getHALRegistredPapers()
hal.removeDuplicates()


