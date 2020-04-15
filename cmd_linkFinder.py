import requests
from bs4 import BeautifulSoup
import sys


if len(sys.argv) >=2 :
    #include url with http/https
    url = sys.argv[1]
    page = requests.get(url)
    if page.status_code == 200:
        print('URL good to go')
    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find_all("a")
    print('total links found:',end='')
    print(len(a))
    print("Broken links:\n=======================================================\n")

    for i in range(len(a)):
        string = a[i]['href']
        if string[0:4] != 'http':
            link = url+string
            try:
                if requests.get(link).status_code != 200:
                    print(link,end='\n\n\n')
            except:
                print(link)
                pass
        else:
            link = string
            try:
                if requests.get(link).status_code != 200:
                    print(link,end='\n\n\n')
            except:
                print(link)
                pass
else:
    print('No argument passed')