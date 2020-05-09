from selenium import webdriver
import pandas as pd

path_to_chromedriver = './chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://www.reta-vortaro.de/revo/'
browser.get(url)
browser.switch_to.frame('indekso')

allwords = []
boldwords = []
letters = ['a', 'b', 'c', 'ĉ', 'd', 'e', 'f', 'g', 'ĝ', 'h', 'ĥ', 'i', 'j', 'ĵ',
           'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'ŝ', 't', 'u', 'ŭ', 'v', 'z']

for letter in letters:
    browser.find_element_by_link_text(letter).click()
    elements = browser.find_element_by_class_name('enhavo').find_elements_by_xpath("//a[contains(@href, '/art/')]")
    for element in elements:
        allwords.append((element.text, element.get_attribute('href')))
    elements = browser.find_element_by_class_name('enhavo').find_elements_by_xpath("//a[contains(@href, '/art/')]/b//ancestor::a")
    for element in elements:
        boldwords.append((element.text, element.get_attribute('href')))

pd.DataFrame.from_records(allwords).to_csv('revo.csv', header=False, index=False)
pd.DataFrame.from_records(boldwords).to_csv('revo_radikoj.csv', header=False, index=False)