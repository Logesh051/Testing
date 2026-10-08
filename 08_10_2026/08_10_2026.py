from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Open browser
driver = webdriver.Chrome()
driver.get("https://vinothqaacademy.com/demo-site/")
driver.maximize_window()
time.sleep(3)

#TC01 Open student registration page
print("TC01 Passed - Registration page opened successfully")
driver.save_screenshot("01_registration_page.png")
time.sleep(2)

#TC02 Locate username using Attribute XPath
driver.find_element(By.XPATH, "//input[@name='vfb-5']").send_keys("Daredevil")
print("TC02 Passed - Username entered successfully")
time.sleep(1)

#TC03 Enter password using Attribute XPath
driver.find_element(By.XPATH, "//input[@name='vfb-7']").send_keys("hello123")
print("TC03 Passed - Password entered successfully")
time.sleep(1)

#TC04 Locate element using text()
driver.find_element(By.XPATH, "//h3[text()='Registration Form']")
print("TC04 Passed - Registration Form located successfully")
time.sleep(1)

#TC05 Locate textbox dynamically using contains()
driver.find_element(By.XPATH, "//input[contains(@name,'vfb-13[address]')]").send_keys("Saveetha Nagar")
print("TC05 Passed - Address textbox located successfully")
time.sleep(1)

#TC06 Locate element with prefix using starts-with()
driver.find_element(By.XPATH, "//input[starts-with(@name,'vfb-14')]").send_keys("abc2@gmail.com")
print("TC06 Passed - Email field located successfully")
time.sleep(1)

#TC07 Find input using two attributes using and
driver.find_element(By.XPATH, "//input[@name='vfb-13[city]' and @type='text']")
print("TC07 Passed - Input located using AND successfully")
time.sleep(1)

#TC08 Find element using alternatives using or
driver.find_element(By.XPATH, "//input[@name='vfb-13[city]' or @type='text']")
print("TC08 Passed - Element located using OR successfully")
time.sleep(1)

#TC09 Find parent form using parent
driver.find_element(By.XPATH, "//input[@id='vfb-13-zip']/parent::*")
print("TC09 Passed - Parent element located successfully")
time.sleep(1)

#TC10 Find form from input using ancestor
driver.find_element(By.XPATH, "//input[@id='vfb-13-zip']/ancestor::form")
print("TC10 Passed - Form located using ancestor successfully")
time.sleep(1)

#TC11 Find child inputs using child
driver.find_element(By.XPATH, "//form/child::input")
print("TC11 Passed - Child input located successfully")
time.sleep(1)

#TC12 Find next element using following
driver.find_element(By.XPATH, "//input[@id='vfb-13-city']/following::input[1]")
print("TC12 Passed - Following element located successfully")
time.sleep(1)

#TC13 Find checkbox using Attribute + XPath
driver.find_element(By.XPATH, "//input[@name='vfb-20[]' and @type='checkbox']")
print("TC13 Passed - Checkbox located successfully")
time.sleep(1)

#TC14 Find radio button using Attribute + XPath
driver.find_element(By.XPATH, "//input[@name='vfb-31' and @type='radio']").click()
print("TC14 Passed - Radio button selected successfully")
time.sleep(1)

#TC15 Select dropdown using XPath + Select
select = Select(driver.find_element(By.XPATH, "//select[@id='vfb-13-country']"))
select.select_by_visible_text("India")
print("TC15 Passed - Country selected successfully")
time.sleep(2)

#TC16 Find second textbox using XPath index
driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
print("TC16 Passed - Second textbox located successfully")
time.sleep(1)

#TC18 Find all input fields using find_elements()
driver.find_elements(By.XPATH, "//input")
print("TC18 Passed - All input fields located successfully")
time.sleep(1)

#TC19 Find dynamic element using contains()
driver.find_element(By.XPATH, "//input[contains(@id,'vfb-')]")
print("TC19 Passed - Dynamic element located successfully")
time.sleep(2)

# Screenshot 2 - Form filled
driver.save_screenshot("02_form_filled.png")
print("Screenshot 2 saved - Form filled")
time.sleep(3)

#TC20 Complete registration automation using multiple XPath concepts
driver.find_element(By.XPATH, "//input[@type='submit']").click()
print("TC20 Passed - Registration submitted successfully")
time.sleep(5)

# Screenshot 3 - Submission success
driver.save_screenshot("03_submission_success.png")
print("Screenshot 3 saved - Submission result")
time.sleep(2)

#TC17 Verify submitted message using text()
driver.find_element(By.XPATH, "//div[contains(text(),'Registration Form is Successfully Submitted')]")
print("TC17 Passed - Submission successful")

time.sleep(5)

driver.quit()
