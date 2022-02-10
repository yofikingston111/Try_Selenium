from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


options = Options()
options.headless = False
# options.add_argument('window-size=1920x1080')


url = 'https://www.audible.com/search?page=4&ref=a_search_c4_pageNext&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=PV7NESXP2RM6J3WR5QHR'
path = 'D:\github\Try_selenium\chromedriver.exe'

driver = webdriver.Chrome(path, options=options)
driver.get(url)
driver.maximize_window()

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)


# current page
current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    # time.sleep(2)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container' )))
    # container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './li')))
    # products = container.find_elements_by_xpath('./li')

    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
    current_page = current_page + 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton ")]')
        next_page.click()
    except:
        pass
driver.quit()
# print(products.text)
8

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_headless.csv', index=False)
