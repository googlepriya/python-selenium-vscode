from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


print(driver.title)


# Maximize the browser window
driver.maximize_window()


# Wait for the page to load
time.sleep(2)


# Locate the username password and Login fields
username_input = driver.find_element(By.NAME,"username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH,"//button[@type='submit']")


# Enter credentials (use demo credentials provided by OrangeHRM) and click the login button
username_input.send_keys("Admin")
password_input.send_keys("admin123")
login_button.click()


# Wait for the dashboard page to load and check for a specific element
try:
    # Explicit wait to ensure the element has time to appear
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    print("Login successful! Dashboard is displayed.")
except:
    print("Login failed. Dashboard is not displayed.")


# Optional: Pause for a while to manually inspect the dashboard
time.sleep(5)


input("Press Enter to close the browser...")
