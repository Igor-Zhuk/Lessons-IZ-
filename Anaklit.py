from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://uk.wikipedia.org')

seach_form = driver.find_element_by_id('searchInput')
seach_form.send_keys('список римських пап')

seach_button = driver.find_element_by_id('searchButton')
seach_button.click()

# Далі допрацюю

