from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://www.saucedemo.com/")

username=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"user-name")
    )
)
username.send_keys("standard_user")

password=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"password")
    )
)
password.send_keys("secret_sauce")

Login=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"login-button")
    )
)

Login.click()
print("Login Success")


add_product_01=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"add-to-cart-sauce-labs-backpack")
    )
)

add_product_01.click()

driver.execute_script("window.scrollBy(0,500);")


add_product_02=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"add-to-cart-sauce-labs-fleece-jacket")
    )
)
add_product_02.click()

print("Product Added Success")

#driver.execute_script("window.scrollto(0,0);")

cart=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"shopping_cart_container")
    )
)

cart.click()
print(driver.current_url)

removeitem=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"remove-sauce-labs-fleece-jacket")
    )
)

removeitem.click()

checkout=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"checkout")
    )
)

checkout.click()

driver.switch_to.new_window('tab')
driver.get("https://demo.automationtesting.in/")

print(driver.current_url)


signin=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"btn2")
    )
)
signin.click()

print("Signin success")

print(driver.current_url)

switch_to=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="SwitchTo"]')
    )
)
switch_to.click()
alert_key=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="Alerts"]')
    )
)

alert_key.click()

print(" alert Selected")

alert_cancel=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="Alert with OK & Cancel "]')
    )
)
alert_cancel.click()

alert_btn=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="click the button to display a confirm box "]')
    )
)

alert_btn.click()

alert=wait.until(
    EC.alert_is_present()
)
alert.accept()

print("Accept Success")

alert_btn_cancel=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="click the button to display a confirm box "]')
    )
)

alert_btn_cancel.click()

alert_cancel=wait.until(
    EC.alert_is_present()
)
alert_cancel.dismiss()

print("Dismiss Success")


alert_textbox=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="Alert with Textbox "]')
    )
)
alert_textbox.click()

prompt_btn=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="click the button to demonstrate the prompt box "]')
    )
)
prompt_btn.click()

alert_prompt=wait.until(
    EC.alert_is_present()
)

alert_prompt.send_keys("HAREESH")
alert_prompt.accept()

print("Prompt Alert Success")

driver.switch_to.new_window('tab')

driver.get("https://www.saucedemo.com/")

username02=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"user-name")
    )
)
username02.send_keys("standard_user")

password02=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"password")
    )
)
password02.send_keys("secret_sauce")

Login02=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"login-button")
    )
)

Login02.click()
print("Login Success")

product_double_click=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="Sauce Labs Backpack"]')
    )
)

ActionChains(driver).double_click(product_double_click).perform()

print("Double function Success")
