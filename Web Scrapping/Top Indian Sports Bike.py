from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Indian Sports Bike'
sheet.append(['Model','Rating (out of 5)','Reviews','Engine (cc)','Torque (bhp)','Weight (kg)','Price (₹)'])

try:
    url = 'https://www.bikewale.com/best-sports-bikes-in-india/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    source = requests.get(url, headers = headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    bikes = soup.find('div', class_='grid-12 alpha omega padding-left20 margin-top20 margin-bottom20').find_all('li')

    for bike in bikes:
        try:

            model = bike.find('h3').a.text
            rating = bike.find('span', class_='rate-star-color').text
            reviews = bike.find('span', class_='review-left-divider').text
            engine = bike.find('div', class_='text-xt-light-grey font14 margin-bottom15').text.split(' cc')[0]
            torque = bike.find('div', class_='text-xt-light-grey font14 margin-bottom15').text.split(' bhp')[0].split(', ')[-1]
            weight = bike.find('div', class_='text-xt-light-grey font14 margin-bottom15').text.split(' kg')[0].split(', ')[-1]
            price = bike.find('div', class_='text-bold').text.split('onwards')[0]
            
            print(f'{model} || {rating} || {reviews} || {engine} || {torque} || {weight} || {price}')
            
            sheet.append([model, rating, reviews, engine, torque, weight, price])

        except:
            pass

except Exception as e:
    print(e)

excel.save('Top Indian Sports Bike.xlsx')