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
                divs_name=soup.find_all('article')
                for div in divs_name:
                    title = div.find('a').text.strip()
                    try:
                        description = div.find('p').text.strip()
                    except:
                        description = ''
                        pass
                    link = div.find('a')['href']
                    list_div.append({"title" : title, "description" : description, 'link': link, 'slug': filename})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
