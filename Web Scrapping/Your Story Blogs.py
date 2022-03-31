from bs4 import BeautifulSoup
import requests
import openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Blogs'
sheet.append(['Title', 'Date Posted', 'Category', 'Link'])


url = 'https://yourstory.com/tag/blog'

source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')

blogs = soup.find_all('div', class_ ='sc-dlnjwi sc-ehALMs kTFpSf carCnm')

for blog in blogs:
    try:

        title = blog.find('div', class_='sc-hkeOVe ieyypA').get_text(strip=True)
        posted_on = blog.find('span', class_='sc-jcwpoC ebZvuV').text
        category = blog.find('span', class_='sc-gVFcvn FwmRi').text
        link_src = blog.a['href']
        link = f'https://yourstory.com{link_src}'
        
        print(f'{title} || {posted_on} || {category} || {link}')
        print()
        sheet.append([title, posted_on, category, link])


    except:
        pass

excel.save('Your Story Blogs.xlsx')

