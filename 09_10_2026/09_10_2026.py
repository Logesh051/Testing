
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://assertqa.com/practice/webtables")
driver.maximize_window()
time.sleep(1)

table = driver.find_element(By.ID, "employees-table")
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

#TC01 Print all column headings
headings = driver.find_elements(By.XPATH, "//th")
print("\nTC01 - Table Headings:")
for heading in headings:
    print(heading.text)

#TC02 Print the first data row
print("\nTC02 - First Employee Record:")
first_row = rows[0]
cells = first_row.find_elements(By.TAG_NAME, "td")
for cell in cells:
    print(cell.text)

#TC03 Print the last data row
print("\nTC03 - Last Employee Record:")
last_row = rows[-1]
cells = last_row.find_elements(By.TAG_NAME, "td")
for cell in cells:
    print(cell.text)

#TC04 Search employee by last name
search_name = "Martinez"
print("\nTC04 - Search by Last Name:")
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if cells[2].text == search_name:
        for cell in cells:
            print(cell.text)
        found = True
        break

if not found:
    print("Employee not found")

#TC05 Extract all email addresses
print("\nTC05 - Email Addresses:")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    print(cells[3].text)

#TC06 Find employee with highest Salary
print("\nTC06 - Highest Salary:")
highest_salary = -1
highest_employee = ""

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    salary = int(cells[5].text.replace("$", "").replace(",", ""))

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = cells[1].text + " " + cells[2].text

print("Employee:", highest_employee)
print("Salary: $", format(highest_salary, ","), sep="")

#TC07 Verify a website link exists
print("\nTC07 - Website Link Check:")
links = driver.find_elements(By.XPATH, "//a[@href]")
if len(links) > 0:
    print("PASS - Website link exists")
else:
    print("FAIL - Website link not found")

#TC08 Count data rows without header
print("\nTC08 - Total Data Rows:")
print("Number of rows:", len(rows))

time.sleep(2)
driver.quit()
