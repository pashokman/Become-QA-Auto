""" Here I learned how to use POM to the scenario from "test_first_ui.py". """

import pytest


@pytest.mark.git_hub_ui
def test_page_title(sign_in_page):
    # Open page
    sign_in_page.go_to()

    # Check page title
    assert sign_in_page.get_title() == "Sign in to GitHub · GitHub"


@pytest.mark.git_hub_ui
def test_incorrect_username_and_password_error_message(sign_in_page):
    # Open page
    sign_in_page.go_to()

    # Enter nonexisting username/email and password, click on "login" btn
    sign_in_page.try_login("wrongaddres@mail.com", "wrongpassword")
    error_message = sign_in_page.get_err_message()
    
    assert error_message.text == "Incorrect username or password."
