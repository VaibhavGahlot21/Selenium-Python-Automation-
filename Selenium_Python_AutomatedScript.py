from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")

wait = WebDriverWait(driver, 10)

#Search for "men tshirt"
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("men tshirt")
search_box.send_keys(Keys.RETURN)

#Click on the 4th product
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.s-main-slot div[data-component-type="s-search-result"]')))
products = driver.find_elements(By.CSS_SELECTOR, 'div.s-main-slot div[data-component-type="s-search-result"]')
if len(products) >= 4:
    product = products[3]
    link = product.find_element(By.TAG_NAME, "a")
    link.click()
else:
    print("Less than 4 products found.")
    driver.quit()
    exit()

#Switch to new tab
driver.switch_to.window(driver.window_handles[1])

#Select size "L" if available
try:
    size_L = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='L' and contains(@class, 'a-button-text')]")))
    size_L.click()
    print("Size 'L' selected.")
except:
    print("Size 'L' not found or not clickable.")

#Add to Cart
try:
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_btn.click()
    print("Product added to cart.")
except:
    print("Add to Cart button not found.")
    driver.quit()
    exit()

#Go to Cart
cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
cart_btn.click()

#Delete the item from cart
try:
    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Delete"]')))
    delete_btn.click()
    print("Item removed from cart.")
except:
    print("Delete button not found.")

#Verify Cart is Empty
time.sleep(3)
try:
    empty_msg = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Your Amazon Cart is empty")]')))
    print("Cart is empty.")
except:
    print("Cart is not empty or layout changed.")

#Show alert and close
driver.execute_script("alert('Signin before shopping !!!!!');")
time.sleep(5)
driver.quit()
