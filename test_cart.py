from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 🔥 STOP here for manual login
    input("👉 Enter username & password manually, then press ENTER here...")

    wait = WebDriverWait(driver, 10)

    # Wait for inventory page after login
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Add to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify item
    item = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "inventory_item_name")
    )).text

    if item == "Sauce Labs Backpack":
        print("Add to Cart Test Passed ✅")
    else:
        print("Add to Cart Test Failed ❌")

finally:
    input("Press Enter to close browser...")
    driver.quit()