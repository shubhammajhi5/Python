import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Courses'
sheet.append(['Released Date','Title','Description'])

try:

    source = requests.get('https://www.codewithharry.com/blog/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    courses = soup.find_all('div', class_ = 'mt-6')

    for course in courses:

        try:

            rel_date = course.find('span', class_= 'font-light text-gray-600').text
            title = course.find('span', class_= 'text-2xl font-bold text-gray-700').a.text
            description = course.find('p', class_= 'mt-2 text-gray-600').text

            print(rel_date)
            print(title)
            print(description)
            print()

            sheet.append([rel_date, title, description])

        except:
            pass

except Exception as e:
    print(e)

excel.save('Code With Harry Blogs.xlsx')