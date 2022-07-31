# downloads every single xkcd comics

import requests
import os
from bs4 import BeautifulSoup

os.makedirs('XKCD', exist_ok = True)

url = 'https://xkcd.com/'

while not url.endswith('#'):
    # download the page
    print(f'Downloading page {url}')

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find Comic Image !!!')
    else:
        comicURL = 'https:' + comicElem[0].get('src')
        # download the image
        print(f'Downloading image {comicURL}')
        res = requests.get(comicURL)
        res.raise_for_status()

        # save the image to ./XKCD
        imageFile = open(os.path.join('XKCD', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev buttons url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done...')

    
