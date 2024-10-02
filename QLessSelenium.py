from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import tkinter as tk
from tkinter import ttk
import time
import time
from datetime import datetime


# Create the main application window
root = tk.Tk()
root.title("Student Interaction Form")

# Define StringVar and IntVar fields for text and dropdown inputs
firstName = tk.StringVar()
lastName = tk.StringVar()
phoneNum = tk.StringVar()  # Changed from IntVar to StringVar for validation
studentID = tk.StringVar()  # Changed from IntVar to StringVar for validation
emailAddress = tk.StringVar()  # New email field
interactionOption = tk.StringVar()
serviceOption = tk.StringVar()

# Options for the dropdowns
interaction_options = ['Telephone Call', 'In Person Meeting']
service_options = [
    "New Enrollments", "Course Prerequisites", "EECS GPA",
    "General Inquiries", "Lab/Tutorial Change", "Section Change", 
    "Transfer Credits", "Waitlist Results"
]

# Validation function to allow only integers
def validate_integer(value):
    if value.isdigit() or value == "":  # Allow digits and empty field
        return True
    return False

# Register the validation function
vcmd = (root.register(validate_integer), '%P')

# Define the labels and input fields for the form
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=firstName).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=lastName).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=phoneNum, validate="key", validatecommand=vcmd).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Student ID").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=studentID, validate="key", validatecommand=vcmd).grid(row=3, column=1, padx=10, pady=5)

# Add the email address field
tk.Label(root, text="Email Address").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=emailAddress).grid(row=4, column=1, padx=10, pady=5)

# Dropdown for Interaction Type
tk.Label(root, text="Interaction Type").grid(row=5, column=0, padx=10, pady=5)
interaction_menu = ttk.Combobox(root, textvariable=interactionOption)
interaction_menu['values'] = interaction_options
interaction_menu.grid(row=5, column=1, padx=10, pady=5)

# Dropdown for Service Option
tk.Label(root, text="Service Option").grid(row=6, column=0, padx=10, pady=5)
service_menu = ttk.Combobox(root, textvariable=serviceOption)
service_menu['values'] = service_options
service_menu.grid(row=6, column=1, padx=10, pady=5)

# Submit button and action
def submit_form():
    print(f"First Name: {firstName.get()}")
    print(f"Last Name: {lastName.get()}")
    print(f"Phone Number: {phoneNum.get()}")
    print(f"Student ID: {studentID.get()}")
    print(f"Email Address: {emailAddress.get()}")
    print(f"Interaction Type: {interactionOption.get()}")
    print(f"Service Option: {serviceOption.get()}")
    root.destroy()  # Close the GUI after submission

tk.Button(root, text="Submit", command=submit_form).grid(row=7, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()

def serviceOptionID():
    if (serviceOption.get() == "New Enrollments"):
        return "tt9000004112"
    elif (serviceOption.get() == "Course Prerequisites"):
        return "tt9000004113"
    elif (serviceOption.get() == "EECS GPA"):
        return "tt9000004114"
    elif (serviceOption.get() == "General Inquiries"):
        return "tt9000004115"
    elif (serviceOption.get() == "Lab/Tutorial Change"):
        return "tt9000004116"
    elif (serviceOption.get() == "Section Change"):
        return "tt9000004117"
    elif (serviceOption.get() == "Transfer Credit"):
        return "tt9000004118"
    elif (serviceOption.get() == "Waitlist Result"):
        return "tt9000004119"
# Specify the desired time (24-hour format)
target_time = "22:09"  

# Function to check the current time
def wait_until_target_time(target_time):
    while True:
        # Get the current time in HH:MM format
        current_time = datetime.now().strftime("%H:%M")
        
        # Check if the current time matches the target time
        if current_time == target_time:
            print("It's time! Starting the bot.")
            break
        
        # Sleep for 30 seconds before checking again to avoid overloading the CPU
        time.sleep(15)

# Wait until the specified time
wait_until_target_time(target_time)

# Your bot code starts here
print("Bot is running...")
# (Bot logic)
# Read the file path directly from the .env file
file_path = open('.env').read().strip()

service = Service(executable_path=file_path)
driver = webdriver.Chrome(service=service)

driver.get("https://kiosk.ca1.qless.com/kiosk/app/home/19713")
time.sleep(5)
print(phoneNum.get())
# Check for the element with the specified class name
try:
    
    # Replace 'element_selector' with the actual selector for the element you want to check
    element = driver.find_element(By.CLASS_NAME, "is-desktop")
    # If found, skip the execution of the specific part
    print("Element with class 'is-desktop' found.")
    input_element = driver.find_element(By.ID, "consumerfield_firstName")
    input_element.send_keys(firstName.get())

    #last name and phone number
    input_element = driver.find_element(By.ID, "consumerfield_lastName")
    input_element.send_keys(lastName.get())

    input_element = driver.find_element(By.ID, "consumerfield_phone")
    input_element.send_keys(phoneNum.get())

    time.sleep(1)

    input_element.send_keys(Keys.ENTER)

    time.sleep(1)
    # student number
    input_element = driver.find_element(By.ID, "customscreenfield_StudentID")
    input_element.send_keys(studentID.get())
    time.sleep(1)
    input_element.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # telephone cant get option value so if statment to choose the option
    if (interactionOption.get() == "Telephone Call"):
        input_element = Select(driver.find_element(By.ID, "customscreenfield_Interaction_0"))
        input_element.select_by_value("Telephone Call")  
    else:
        input_element = Select(driver.find_element(By.ID, "customscreenfield_Interaction_0"))
        input_element.select_by_value("In person Meeting")  

    time.sleep(1)
    input_element = driver.find_element(By.ID, "customscreenfield_Email_0")
    input_element.send_keys(emailAddress.get())
    
    input_element.send_keys(Keys.ENTER)
    time.sleep(1)

    input_element = driver.find_element(By.ID, serviceOptionID()).click()
    time.sleep(5)
        
except Exception as e:
    # If the element is not found, dont run the desired code
    print("Element with class 'is-desktop' not found.")

driver.quit