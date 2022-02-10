from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = './chromedriver.exe'


driver = webdriver.Chrome(path)
driver.get(website)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
dom = etree.HTML(str(soup))

all_matches_button = dom.xpath('//label[@analytics-event="All matches"]')
print(all_matches_button)