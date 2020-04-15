import pytest
import time
import json
import pandas as pd
from selenium.webdriver.chrome.options import Options#chrome  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chrome_options = Options()  
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get('https://www.covid19india.org/')
time.sleep(7)
l=driver.find_elements_by_xpath('//div[@class="table__title-wrapper"]')
k=driver.find_elements_by_xpath('//span[@class="table__count-text"]')

values=[]
for i in k:
	values.append(i.text)
while True:
	try:
		values.remove('')
	except:
		break

for i in values:
	if(i=='-'):
		values[values.index(i)]=0

temp=0
data=[]
for i in (l):
	td=[0]*4
	td[0]=i.text
	td[1]=values[temp]
	td[2]=values[temp+1]
	td[3]=values[temp+2]
	data.append(td)
	temp+=3

df=pd.DataFrame(data,columns=['State','Confirmed','Active','Recovered'])
print(df.head(len(data)))
