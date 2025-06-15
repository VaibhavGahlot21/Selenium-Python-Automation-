from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

#Login
driver.get("https://opensource-demo.orangehrmlive.com/")
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Logged in")
time.sleep(4)

#Navigate to PIM - Add Employee
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))).click()
time.sleep(4)

#Fill the form
wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Steve")
driver.find_element(By.NAME, "lastName").send_keys("Smith")
print("📝 Employee name filled")
time.sleep(4)

#Toggle switch
toggle = driver.find_element(By.XPATH, "//span[contains(@class,'oxd-switch-input')]")
toggle.click()
print("🔄 Login detail toggle clicked")
time.sleep(4)

#Enter login details for new employee
driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div/input").send_keys("steve_test")
driver.find_element(By.XPATH, "//label[text()='Password']/../following-sibling::div/input").send_keys("steve@123")
driver.find_element(By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input").send_keys("steve@123")
print("Login credentials entered")
time.sleep(4)

#ActionChains(hover on user icon)
user_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='oxd-userdropdown-tab']")))
ActionChains(driver).move_to_element(user_icon).perform()
print("Hovered over user icon")
time.sleep(4)

#Screenshot saved
os.makedirs("screenshots", exist_ok=True)
driver.save_screenshot("screenshots/hrm_result.png")
print("Screenshot saved.")
time.sleep(4)

driver.quit()
print("Process completed")