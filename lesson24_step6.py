from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"

browser = webdriver.Chrome()

# сообщаем Webdriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)
browser.get(link)

button = browser.find_element_by_id("button")
button.click()
