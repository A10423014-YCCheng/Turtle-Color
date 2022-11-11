from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = 'https://trinket.io/docs/colors'
driver.get(url)

search_field = driver.find_elements(By.CLASS_NAME, 'faux-input')
color_l = []
for item in search_field:
    color_l.append(item.get_attribute('textContent'))
driver.quit()

color = []
Turtle_name = []
CSS_name = []
Hex = []
RGB = []
for i, item in enumerate(color_l):
    if (i % 6 == 3):
        color.append(color_l[i:i + 3])
    elif (i % 6 == 4) or (i % 6 == 5):
        continue
    else:
        color.append(item)

for i, item in enumerate(color):
    if i % 4 == 0:
        Turtle_name.append(item)
    elif i % 4 == 1:
        CSS_name.append(item)
    elif i % 4 == 2:
        Hex.append(item)
    elif i % 4 == 3:
        RGB.append(item)

color_df = pd.DataFrame({'Turtle name': Turtle_name, 'CSS name': CSS_name, 'Hex': Hex, 'RGB': RGB})
color_df = color_df.drop_duplicates(subset=['Turtle name'])
color_df.to_excel('Color.xlsx', index = False, sheet_name='Turtle Color')