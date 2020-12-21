# Import modules

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Create DataFrame and filter unrelevant URLs
def create_df(file):
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    unrelevant = df['URL'].str.contains("/slack")
    df = df[unrelevant == False]
    return df

# Fill in email and submit
def register(email, data):
    i = 0
    succeeded = []
    for url in data['URL']:
        i+=1
        # Open URL in driver
        driver = webdriver.Firefox(executable_path="selenium-firefox/drivers/geckodriver")
        url = url.replace(" ", "")
        driver.get(url)

        # Find first input form and fill in email
        try:
            driver.find_element_by_tag_name('input').send_keys(email, Keys.ENTER)
            succeeded.append(data['Name.'][i])
            time.sleep(1)
        except:
            print(data['Name.'][i], 'Not succeeded')
        if len(succeeded > 0):
            print(i / len(succeeded), 'succeeded')
        else:
            print(0, 'succeeded')
        time.sleep(1)
        driver.quit()
    return succeeded

email = "Davidanthony_84@hotmail.com"
csvfile = "slackgroups.csv"
data = create_df(csvfile)
succeeded = []
register(email, data)