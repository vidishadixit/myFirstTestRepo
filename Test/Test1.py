# Creating separate directory for test is a good coding practice as it will separate the tests from your code and easy for maintainance

from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\pc1\\PycharmProjects\\SeleniumWithPython\\Library\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("flowers")
driver.find_element_by_class_name("gNO89b").click()
