from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get("http://baidu.com/")
driver.quit()
