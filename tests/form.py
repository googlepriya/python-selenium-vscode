from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")
print("Title:"+driver.title)
#time.sleep(3)
driver.find_element(By.ID,"fullName").send_keys("Gokulapriya S")
driver.find_element(By.ID,"email").send_keys("gokul@gmail.com")
driver.find_element(By.ID,"phoneNumber").send_keys("9090909090")
Position = Select(driver.find_element(By.ID,"desiredPosition"))
Position.select_by_visible_text("Designer")
driver.find_element(By.ID,"location1").click()
driver.find_element(By.ID,"experienceYears").send_keys("4")
driver.find_element(By.ID,"skill1").click()
driver.find_element(By.ID,"skill2").click()
driver.find_element(By.ID,"skill3").click()
driver.find_element(By.XPATH,"//button[text()='Submit Application']").click()
time.sleep(3)
success_message = driver.find_element(By.ID, "successMessage").text
assert "Submission successful!" in success_message
print(success_message)
time.sleep(3)
input("Press Enter to close the browser...")



