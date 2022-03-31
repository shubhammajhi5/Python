import requests
import openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Corey_MS Courses'
sheet.append(['Course Title','Released Date','Filed Under','Tagged With', 'Video Link'])

try:
    source = requests.get('https://coreyms.com/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    
    courses = soup.find('main', class_='content').find_all('article')

    for course in courses:

        try:
        
            course_title = course.find('header', class_='entry-header').h2.text
            date_released = course.find('header', class_='entry-header').p.text.split(' by')[0]
            link_code = course.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
            link = f'https://www.youtube.com/watch?v={link_code}'
            filed_under = course.find('footer').find('span', class_='entry-categories').text.split(': ')[1]
            tagged_with = course.find('footer').find('span', class_='entry-tags').text.split(': ')[1]

            print(course_title, date_released, filed_under, tagged_with, link)
            sheet.append([course_title, date_released, filed_under, tagged_with, link])

        except:
            pass


except Exception as e:
    print(e)
    

excel.save('CoreyMS Courses.xlsx')