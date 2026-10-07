from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
wait=WebDriverWait(driver,10)

driver.maximize_window()

login=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="nav-link-accountList"]/button')
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    login
)

driver.execute_script(
        "arguments[0].click();",
    login
)
print("login clicked success")
signin=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="nav-flyout-ya-signin"]/a/span')
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    signin
)

driver.execute_script(
        "arguments[0].click();",
    signin
)
print("signin success")
mobile=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"ap_email_login")
    )
)
mobile.click()
mobile.send_keys("8901111112189")
button=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="continue"]/span/input')
    )
)
button.click()
print("success")

password=wait.until(
    EC.element_to_be_clickable(
        (By.ID,'ap_password')
    )
)
password.send_keys("aamaoznmazon")

signin=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"signInSubmit")
    )
)
signin.click()

print("Login Successfully")

searchbox=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"twotabsearchtextbox")
    )
)
searchbox.send_keys("Bag")
searchbox.click()

searchicon=wait.until(
    EC.element_to_be_clickable(
        (By.ID,"nav-search-submit-button")
    )
)
searchicon.click()

print("Product Shown Success")

driver.execute_script("window.scrollBy(0,500);")

productPage = wait.until(
    EC.element_to_be_clickable
        (
            (By.XPATH, "//span[contains(text(),'Aristocrat Nova 15L Laptop Backpack (15.6\"), 2 Com')]")
        )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    productPage
)

productPage.click()

print("Product clicked")

wait.until(lambda d: len(driver.window_handles) > 1)

driver.switch_to.window(driver.window_handles[-1])

print("Product page opened")
print("Current URL:", driver.current_url)

cartbutton=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//input[@id="add-to-cart-button"]')
    )
)

cartbutton.click()
print("cart added success")

gotocart=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="sw-gtc"]/span/a')
    )
)
gotocart.click()

print("gotocart success")

proceed=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="sc-buy-box-ptc-button"]/span/input')
    )
)

proceed.click()

time.sleep(30)
