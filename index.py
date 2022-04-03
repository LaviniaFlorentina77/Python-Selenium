from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()
driver.get('https://weather.com/ro-RO/vreme/astazi/l/ROXX0003:1:RO')
driver.implicitly_wait(30)
#accept cookies
my_element = driver.find_element_by_id('truste-consent-button')
my_element.click()
driver.implicitly_wait(10)
#details
driver.get('https://weather.com/ro-RO/weather/hourbyhour/l/d47adb5123610c56b41dcb43c498eb3c8df0591918ce1d678bb6cbac3f50e386')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")