# web-scraping
import requests
from bs4 import BeautifulSoup

def webscraper():
    n=0
    r = []
    while n<50:
        tmp = requests.get("http://3.95.249.159:8000/random_company").text    
        r = r + [tmp]
        n=n+1

    x=[]
    H=[]
    for i in r:
        soup = BeautifulSoup(i, 'html.parser')
        x.append(soup.find('li').text)
        v= soup.get_text()
        k = v.splitlines()
    
        for j in k:
            if j.startswith('Purpose'):
                H.append(j)

    z = open("hw2results.txt", "a") 

    for i in x:
        z.write(i + "\n")
    z.close()  
    z = open("hw2results.txt", "a") 
      
    for g in H:
        z.write(g + "\n")
    z= open("hw2results.txt", "r")
    z.read()
    z.close()     

if __name__ == "__main__": 
    webscraper()
