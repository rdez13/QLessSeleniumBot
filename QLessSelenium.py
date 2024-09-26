from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/Users/Rayamba/Desktop/pyautogui_QLess/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://kiosk.ca1.qless.com/kiosk/app/home/19713")
time.sleep(5)

# Check for the element with the specified class name
try:
    
    # Replace 'element_selector' with the actual selector for the element you want to check
    element = driver.find_element(By.CLASS_NAME, "is-desktop")
    # If found, skip the execution of the specific part
    print("Element with class 'is-desktop' found.")
    input_element = driver.find_element(By.ID, "consumerfield_firstName")
    input_element.send_keys("Ryan")

    input_element = driver.find_element(By.ID, "consumerfield_lastName")
    input_element.send_keys("Dezfuli")

    input_element = driver.find_element(By.ID, "consumerfield_phone")
    input_element.send_keys("647-548-9734")

    time.sleep(1)

    input_element.send_keys(Keys.ENTER)

    time.sleep(1)

    input_element = driver.find_element(By.ID, "customscreenfield_StudentID")
    input_element.send_keys("218826859")

    input_element = driver.find_element(By.ID, "customscreenfield_Interaction_0")
    input_element.send_keys(Keys.ARROW_DOWN)

    input_element = driver.find_element(By.ID, "customscreenfield_Email_0")
    input_element.send_keys("ryandezfuli@yahoo.com")
    
        
except Exception as e:
    # If the element is not found, dont run the desired code
    print("Element with class 'is-desktop' not found.")





driver.quit