import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

website = 'https://www.adamchoi.co.uk/overs/detailed'

driver = webdriver.Chrome()

driver.get(website)

all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(by='id', value='country'))
dropdown.select_by_visible_text('Ukraine')

time.sleep(3)

date = [elem.text for elem in driver.find_elements(by='xpath', value='//tr/td[1]')]
home_team = [elem.text for elem in driver.find_elements(by='xpath', value='//tr/td[3]')]
score = [elem.text for elem in driver.find_elements(by='xpath', value='//tr/td[4]')]
away_team = [elem.text for elem in driver.find_elements(by='xpath', value='//tr/td[5]')]

driver.quit()

df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})
df.to_csv('football_data.csv', index=False)
