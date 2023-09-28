import os
from bs4 import BeautifulSoup

def main():
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('div', {'class': 'col d-flex align-items-stretch mb-3'})
                for div in divs_name:
                    title = div.find('div',{"class":"card-header"}).text.strip()
                    description = div.find('p',{"class":"card-text"}).text.strip()
                    link = div.find('a',{"class":"btn btn-primary btn-sm"})['href']
                    list_div.append({'title':title, 'description': description, 'link':link ,'slug': filename})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
