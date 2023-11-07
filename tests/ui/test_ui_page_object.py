import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(sign_in_page):
    # Create an object for manage browser
    # sign_in_page = SignInPage()

    # # Open page
    # sign_in_page.go_to()

    # # Enter nonexisting username/email and password, click on "login" btn
    # sign_in_page.try_login("wrongaddres@mail.com", "wrongpassword")

    # # Check page title
    # assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # # Close browser
    # sign_in_page.close()

    # change previous strings into 1 string function
    sign_in_page.title_testing("wrongaddres@mail.com", "wrongpassword", "Sign in to GitHub · GitHub")