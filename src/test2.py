from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Oleh/Desktop/chromedriver_win32/chromedriver")

driver.get("https://www.google.com/")

search_button = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")

search_field = driver.find_element_by_xpath("//*[@name='q']")

search_field.send_keys("anime")

search_button.click()

# //*[@name='q']

# //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input

# /html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input

#//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]

