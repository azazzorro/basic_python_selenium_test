from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Oleh/Desktop/chromedriver_win32/chromedriver")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")

search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Test Automation")

search_button.click()

assert "Test Automation" in driver.title

assert "Test 1 Automation" in driver.title

assert "Test 2 Automation" in driver.title

driver.quit()