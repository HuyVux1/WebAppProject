import requests
from bs4 import BeautifulSoup as soup 
import csv

base_url = 'https://www.gettyimages.com/photos/healthy-lungs-ct-scan?phrase=healthy%20lungs%20ct%20scan&sort=mostpopular'
r = requests.get(base_url).text
page_soup = soup(r, 'lxml')
count = 0
articles = page_soup.find('div', id='gallery').find_all('article')

csv_file = open('ctscan.csv', 'w', newline='', encoding='utf-8')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['image source', 'image title'])

for article in articles:
    img_src = article.img['src']
    img_cap = article.img['alt']
    csv_writer.writerow([img_src, img_cap])

csv_file.close()
