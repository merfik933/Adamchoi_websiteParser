from selenium import webdriver

website = "https://www.adamchoi.co.uk/overs/detailed"

path = "D:\Programs\Drivers\chrome-driver"
driver = webdriver.Chrome(path)

driver.get(website)

driver.quit()