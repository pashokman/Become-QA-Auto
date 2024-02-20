"""
Here I learned:
    - how to work with Selenium webdriver; 
    - open page; 
    - find element;
    - enter some value into a field; 
    - click on element; 
    - get text from an element;
    - get page title;
    - add testing in different browsers
"""

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.first_ui
def test_check_incorrect_username():
    # Create an object for manage browser
    driver = webdriver.Chrome()
    # Open page
    driver.get("https://github.com/login")
    # Find login field
    login_elem = driver.find_element(By.ID, "login_field")
    # Enter nonexisting username/email
    login_elem.send_keys("wrongaddres@mail.com")
    # Find password field
    password_elem = driver.find_element(By.ID, "password")
    # Enter wrong password
    password_elem.send_keys("wrongpassword")
    # Find button 'Login'
    btn_login = driver.find_element(By.NAME, 'commit')
    # Click on btn
    btn_login.click()
    # Find error message field
    err_field = driver.find_element(By.CLASS_NAME, 'js-flash-alert')

    assert err_field.text == "Incorrect username or password.", "Error message error"
    assert driver.title == "Sign in to GitHub · GitHub", "First UI page title error"

    # Close browser
    driver.close()