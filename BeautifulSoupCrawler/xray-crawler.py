import requests
from bs4 import BeautifulSoup as soup 
import csv

base_url = 'https://www.kenhub.com/en/library/anatomy/normal-chest-x-ray'
r = requests.get(base_url).text
page_soup = soup(r, 'lxml')

article = page_soup.article

csv_file = open('xray.csv', 'w',newline = '', encoding='utf-8')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['image source', 'image title'])

for image in article.find_all('img'):
    img_src = image['src']
    img_cap = image['alt'].split(';')[0]
    csv_writer.writerow([img_src, img_cap])

csv_file.close()

