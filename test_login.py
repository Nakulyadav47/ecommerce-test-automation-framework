from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize driver
driver = webdriver.Chrome(service=Service("./chromedriver.exe"))

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validate login
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    if "inventory" in driver.current_url:
        print("Login Test Passed ✅")
    else:
        print("Login Test Failed ❌")

finally:
    input("Press Enter to close browser...")
    driver.quit()