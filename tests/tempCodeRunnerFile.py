from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Add product
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    # Fill details
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Nakul")
    driver.find_element(By.ID, "last-name").send_keys("Yadav")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    driver.find_element(By.ID, "finish").click()

    # Verify success
    message = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )).text

    if "Thank you" in message:
        print("Checkout Test Passed ✅")
    else:
        print("Checkout Test Failed ❌")

finally:
    input("Press Enter to close browser...")
    driver.quit()