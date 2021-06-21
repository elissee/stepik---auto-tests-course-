from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x,y):
    return sum([x, y])

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)

    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)

    z = calc(x,y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(z))

    button = browser.find_element_by_css_selector('[class="btn btn-default"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
