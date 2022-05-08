import requests as r
import json


def findByName(expertName):
    payload = {'name':str(expertName)}
    headers = { 'User-Agent' : 'user_agent', "Cache-Control": "no-cache, max-age=0" }
    url='https://api.aminer.org/api/search/pub/advanced'
    request = r.get(url,headers=headers,params=payload)
    return request.json()
    

file = open('names.txt', 'r')
Lines = file.readlines()
l=0
with open('paper.json', 'w') as outfile:
    for i in Lines:
        l+=1
        json.dump(findByName(i), outfile)
        if l == 4 :
            break

    





