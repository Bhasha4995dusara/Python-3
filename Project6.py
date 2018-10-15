#https://tokensofus.wordpress.com/category/coding/
#for content display in table format
import requests
from bs4 import BeautifulSoup

baseurl = "http://m.imdb.com/feature/bornondate"
imag = []
name = []
film = []
count = 0

try:
    r = requests.get(baseurl,timeout=50)
    #print(r.raise_for_status())
    content = r.text.encode('utf-8', 'ignore')

    soup = BeautifulSoup(r.text,"html.parser")

    for image_loop in soup.find_all('div',class_='lister-item-image')[:10]:
        imag.append(image_loop.img.get("src").strip())

    for name_loop in soup.find_all('h3',class_='lister-item-header')[:10]:
        name.append(name_loop.a.text.strip())

    for film_loop in soup.find_all('p',class_='text-muted text-small')[:10]:
        film.append(film_loop.a.text.strip())

    # for formatting
    for i,j,k in zip(imag,name,film):
        count += 1
        print('-'*50,end='\n')
        print(count,".")
        print("IMAGE : {}".format(i),end='\n')
        print("NAME : {}".format(j),end='\n')
        print("FILM : {}".format(k),end='\n')

except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)