#import libraries
import requests
from bs4 import BeautifulSoup

#extract info from web for 50 times
def webscraper():
    n=0
    r = []
    while n<50:
        tmp = requests.get("http://3.95.249.159:8000/random_company").text    
        r = r + [tmp]
        n=n+1

    sv=[]
    H=[]
    for i in r:
        soup = BeautifulSoup(i, 'html.parser')
        sv.append(soup.find('li').text)
        ve = soup.get_text()
        k = ve.splitlines()
    
        for j in k:
            if j.startswith('Purpose'):
                H.append(j)

    fi = open("hw2results.txt", "a") 

    for i in sv:
        fi.write(i + "\n")
    fi.close()  
    fi = open("hw2results.txt", "a") 
      
    for g in H:
        fi.write(g + "\n")
    fi= open("hw2results.txt", "r")
    fi.read()
    fi.close()     

if __name__ == "__main__": 
    webscraper()
