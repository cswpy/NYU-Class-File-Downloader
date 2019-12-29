from bs4 import BeautifulSoup
import re

def parse_urls(href):
    filePath = href
    with open(filePath,'r') as file:
        content = file.read()
        urls = []
        soup = BeautifulSoup(content,'html.parser')
        links = soup.find_all('a',attrs={'target':'_blank'})
        for link in links:
            url = link.get('href')
            if re.search('access',url) and (url not in urls):
                print(url)
                urls.append(url)
    return urls

