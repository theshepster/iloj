from selenium import webdriver
import pandas as pd

path_to_chromedriver = './chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://www.reta-vortaro.de/revo/'
browser.get(url)
browser.switch_to.frame('indekso')

words = []
letters = ['a', 'b', 'c', 'ĉ', 'd', 'e', 'f', 'g', 'ĝ', 'h', 'ĥ', 'i', 'j', 'ĵ',
           'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'ŝ', 't', 'u', 'ŭ', 'v', 'z']

for letter in letters:
    browser.find_element_by_link_text(letter).click()
    elements = browser.find_element_by_class_name('enhavo').find_elements_by_xpath("//a[contains(@href, '/art/')]")
    for element in elements:
        words.append((element.text, element.get_attribute('href')))
    
pd.DataFrame.from_records(words).to_csv('revo.csv', header=False, index=False)