from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = Service('./chromedriver.exe')

driver = webdriver.Chrome(service=path)
driver.get(website)
# button = driver.find_element_by_class_name("quiz_button")
# button = driver.find_element(By.CLASS_NAME, "quiz_button")



# click on button
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)


matches = driver.find_elements(By.TAG_NAME ,'tr')

date = []
home_team = []
score = []
away_team = []


for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)
driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score':score, 'away_team':away_team})
df.to_csv('football_data.csv', index=False)
df.sort_values(by=['date', 'home_team', 'score', 'away_team'])
print(df)