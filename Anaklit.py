from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://uk.wikipedia.org')

seach_form = driver.find_element_by_css_selector('#searchInput')
seach_form.send_keys('список римських пап')

seach_button = driver.find_element_by_css_selector('#searchButton')
seach_button.click()

pope_cletus = driver.find_element_by_css_selector('div#mw-content-text table:nth-child(9) > tbody > tr:nth-child(5) > td:nth-child(3) > a > img')
pope_cletus.click()


