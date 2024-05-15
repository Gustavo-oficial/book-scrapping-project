import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/"

driver.get(url)
products = driver.find_elements(By.CLASS_NAME, value="product_pod")

titles = []
stocks = []
prices = []
for e in products:
    result = {}
    tagA = e.find_element(By.TAG_NAME, value="h3").find_element(By.TAG_NAME, value="a")

    titles.append(tagA.text)
    tagA.click()
    time.sleep(0.5)
    prices.append(driver.find_element(By.CLASS_NAME, value="price_color").text)
    stocks.append(int(driver.find_element(By.CLASS_NAME, value="instock").text.replace("In stock (", "").replace(" available)", "")))

    driver.back()

data = {"Titulo": titles, "Estoque": stocks,"Price": prices}
dataFrame = pd.DataFrame(data)

dataFrame.to_excel("dados.xlsx")