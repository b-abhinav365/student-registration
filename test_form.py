from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://localhost:8085"

driver = webdriver.Chrome()
driver.get(URL)


def fill_form(name, email, phone, course):
    driver.get(URL)  # reload page for a fresh form
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    if course:
        driver.find_element(By.ID, "course").send_keys(course)
    driver.find_element(By.ID, "submit").click()
    return driver.find_element(By.ID, "message").text


# Test 1: empty form
result = fill_form("", "", "", "")
assert result == "Please fill all fields"
print("Test 1 passed: empty form")

# Test 2: invalid email
result = fill_form("Ravi", "raviemail.com", "9876543210", "CSE")
assert result == "Invalid email"
print("Test 2 passed: invalid email")

# Test 3: invalid phone
result = fill_form("Ravi", "ravi@gmail.com", "12345", "CSE")
assert result == "Phone must be 10 digits"
print("Test 3 passed: invalid phone")

# Test 4: valid data
result = fill_form("Ravi", "ravi@gmail.com", "9876543210", "CSE")
assert result == "Registration successful"
print("Test 4 passed: valid registration")

driver.quit()
print("All tests passed")