from bs4 import BeautifulSoup as bs
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.firefox.options import Options

def getSongUrl(query):
    song = "https://www.youtube.com/results?search_query={}".format(query)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    driver.get(song)
    driver.implicitly_wait(100)

    html = driver.page_source
    result = html.find("watch?")
    result = html[result:result+100]
    result = result.split("\"")
    result = result[0]
    result = "https://youtube.com/{}".format(result)
    return result
