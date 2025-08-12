from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
   
    driver.get("https://demoqa.com/login")
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    ).send_keys("Imranali")

    driver.find_element(By.ID, "password").send_keys("Imran9009@")

    
    login_button = driver.find_element(By.ID, "login")
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    driver.execute_script("arguments[0].click();", login_button)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "submit"))
    )
    print("Login successful!")

    
    driver.get("https://demoqa.com/profile")

   
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName-value"))
    )
    expected_username = "Imranali"
    if username.text == expected_username:
        print(f" Username verified: {username.text}")
    else:
        print(f" Username mismatch: {username.text}")
        raise Exception("Username mismatch!")

    logout_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
    driver.execute_script("arguments[0].click();", logout_button)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    print("Logout successful.")

except Exception as e:
    print(f" Test failed: {e}")

finally:
    time.sleep(2)
    driver.quit()