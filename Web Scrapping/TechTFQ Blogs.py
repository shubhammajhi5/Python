from bs4 import BeautifulSoup
import requests
import openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Blogs'
sheet.append(['Title','Link'])


url = 'https://techtfq.com/blog-1'

source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')

articles = soup.find_all('div', class_ ='summary-title')

for article in articles:
    try:

        title = article.a.text
        link_src = article.a['href']
        link = f'https://techtfq.com{link_src}'

        print(title, '\n', link)
        print()
        sheet.append([title, link])


    except:
        pass

excel.save('TechTFQ Blogs.xlsx')

