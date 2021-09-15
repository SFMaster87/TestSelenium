import time
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
searchName = 'Болгарка'

def main():
    driver = webdriver.Chrome()
    driver.get("https://leroy-spb.com/")
    sercheBtn = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/div[1]')
    sercheBtn.click()
    time.sleep(2)
    product = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/header/div[1]/div[2]/div/div/div[1]/div/div/div[2]/input')
    product.send_keys(searchName)
    product.send_keys(Keys.RETURN)
    time.sleep(2)
    sercheBtn.click()
    time.sleep(2)
    containerNames = driver.find_elements_by_class_name('lux_el__title') #   список названий
    listPrices = driver.find_elements_by_class_name('lux_el__price')    #   список цен
    list = []
    for item in listPrices:
        masStr= item.text.split(" ")
        str = ""
        if masStr[0].isdigit():
            str += masStr[0]
        if  masStr[1].isdigit():
            str += masStr[1]
        if masStr[2].isdigit():
            str += masStr[2]
        list.append(int(str))
    #--------
    listPages = driver.find_elements_by_class_name('v-pagination__item')
    for i in listPrices:
        print(i.text)
    #--------
    minPrice = max(list)
    index: int = list.index(minPrice)
    obj = containerNames[index]
    obj.click()
    time.sleep(10)

if __name__ == '__main__':
    main()