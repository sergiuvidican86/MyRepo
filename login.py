import time

from selenium import webdriver
from selenium.webdriver.common.by import by

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\Bella\\Desktop\\chromedriver.exe")

class testingLogin():

    def loginNOK(self, username, parola:



        driver.get("https://www.demo.guru99.com/v4/")

        # user = driver.find_element_by_name("uid")
        # user = driver.find_element_by_xpath("//input[@name='uid']")
        user = driver.find_element(by.XPATH, "//input[@name='uid']")
        user.send_keys(username)

        # password = driver.find_element_by_name("password")
        # password = driver.find_element_by_xpath("//input[@name='password']")
        password = driver.find_element(by.XPATH, "//input[@name='uid']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        password = driver.find_element_by_xpath("//input[@name='password']")
        button.click()

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("test case login fail")
        except:
            print("test case login pass")



    def loginOK(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=options,executable_path="C:\\Users\\Bella\\Desktop\\chromedriver.exe")

        driver.get("https://www.demo.guru99.com/v4/")

        #user = driver.find_element_by_name("uid")
        #user = driver.find_element_by_xpath("//input[@name='uid']")
        user = driver.find_element(by.XPATH, "//input[@name='uid']")
        user.send_keys("mngr327236")

        #password = driver.find_element_by_name("password")
        #password = driver.find_element_by_xpath("//input[@name='password']")
        password = driver.find_element(by.XPATH, "//input[@name='uid']")
        password.send_keys("rehavAs")

        button = driver.find_element_by_name("btnLogin")
        password = driver.find_element_by_xpath("//input[@name='password']")
        button.click()

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("test case login pass")
        except:
            print("test case login failed")







test = testingLogin()
test.loginOK()

#username = "mngr327236"
#parola = "parolaNOK"
test.loginNOK("mngr327236", "parolaNOK")
test.loginNOK("userNOK", "rehavAs")
test.loginNOK("userNOK", "parolaNOK")
test.loginNOK("", "rehavAs")
test.loginOK("mngr327236", "")

driver.quit()