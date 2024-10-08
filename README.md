
# QLess Virtual Queue Bot

## Overview

The QLess Virtual Queue Bot is a Python-based automation tool designed to help students join a virtual queue on the QLess platform at a pre-scheduled time. By using Selenium for browser automation and a simple Tkinter-based GUI for user input, this bot ensures that students can quickly and easily join the virtual queue without manual intervention.

## Project Details

This bot automates the process of entering the queue by filling out necessary information such as name, student ID, phone number, email, and selecting interaction types and service options. The bot waits until a specified time, then launches a browser to automatically submit the information on the QLess website.

The following steps outline the workflow:

1. **GUI for User Input:**

   - A Tkinter GUI allows users to input personal information such as First Name, Last Name, Phone Number, Student ID, and Email Address.
   - Users can also select from dropdowns for interaction type (e.g., Telephone Call or In-Person Meeting) and service option (e.g., New Enrollments, Course Prerequisites).

2. **Scheduled Automation:**

   - The bot waits until the target time specified by the user.
   - At the scheduled time, Selenium launches a browser, navigates to the QLess website, and inputs the user’s information automatically.

3. **Interaction with QLess:**

   - The bot interacts with the QLess platform by finding and filling out the required fields using Selenium's `find_element` and `send_keys` methods.
   - The bot selects options from the dropdown menus, submits the form, and joins the virtual queue.

## Key Features

- **Automated Queue Entry:** Automatically fills out forms and submits user details to the QLess platform at a scheduled time.
- **Customizable Inputs:** Users can provide details through a simple graphical interface and choose from predefined interaction and service options.
- **Scheduled Execution:** The bot waits until a set time to begin automating the process, ensuring timely entry into the virtual queue.

## Languages Used

- **Python**: Used for both the automation (Selenium) and the GUI (Tkinter) components of the project.

## Tools Used

- **Selenium WebDriver**: Used for automating browser interactions to submit the form on the QLess website.
- **Tkinter**: Provides the graphical user interface for inputting user information.

## Installation Instructions

### Prerequisites

Ensure that you have Python 3.x installed on your machine.

### Install Required Packages

To install the necessary Python packages, run the following commands:

```bash
pip install selenium
pip install tkinter
```

### Setting Up ChromeDriver

Selenium requires a ChromeDriver to interact with the Chrome browser. Follow the steps below to set it up:

1. **Download ChromeDriver**:
   - Visit [ChromeDriver downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and download the version that matches your installed version of Chrome.

2. **Add ChromeDriver to Your Project**:
   - Place the ChromeDriver executable in a known directory.

3. **Set Up .env File**:
   - In the root of the project, create a `.env` file that includes the path to the ChromeDriver executable. For example:

     ```bash
     /path/to/chromedriver
     ```
