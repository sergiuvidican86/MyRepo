import time

from selenium import webdriver

class ChromedriverWindows():

    def searchGoogle(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\Bella\\Desktop\\chromedriver.exe")
        driver.get("https://google.com")

        element = driver.find_element_by_id("jyfHyd")
        element.click()

        element_search = driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()


        time.sleep(30)

        #jyfHyd

search = ChromedriverWindows()
search.searchGoogle()