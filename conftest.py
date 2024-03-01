import pytest
import datetime

# API modules --------------------------------------------------------------------------------------------------------
from modules.api.clients.github import GitHub
from modules.api.clients.pokemon import Pokemon
from modules.api.clients.restfool_booker import RestBooker

# Database module ----------------------------------------------------------------------------------------------------
from modules.common.database import Database

# UI pages modules ---------------------------------------------------------------------------------------------------
# study1
from modules.ui.page_objects.study1.first_ui_page import SignInPage
from modules.ui.page_objects.study1.uakinoclub_page import UAKinoClubPage
from modules.ui.page_objects.study1.herokuapp_page import HerokuAppPage

# study2
from modules.ui.page_objects.study2.general_page import GeneralPage

# Allure reports, screenshots ----------------------------------------------------------------------------------------
import allure
from allure_commons.types import AttachmentType


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Pavlo"
        self.second_name = "Lekhitskyi"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


# API fixtures -------------------------------------------------------------------------------------------------------
@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def pokemon_api():
    api = Pokemon()
    pokemon = api.get_pokemon("ditto")

    yield pokemon


@pytest.fixture
def restbooker():
    api = RestBooker()

    yield api


# Database fixtures --------------------------------------------------------------------------------------------------
@pytest.fixture
def database():
    db = Database()

    yield db


# UI study1 fixtures -------------------------------------------------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser-type", action="store", default="chrome", help="Browser to run tests")

# To run tests in a specific browser should to run command: pytest --browser-type chrome
@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser-type")

# To run tests in all 3 browsers need to run the command: pytest
# @pytest.fixture(params=['chrome', 'firefox', 'edge'])
# def browser_type(request):
#     return request.param


@pytest.fixture
def sign_in_page(browser_type):
    page = SignInPage(browser=browser_type)

    yield page

    page.close()


@pytest.fixture
def uakinoclub(browser_type):
    page = UAKinoClubPage(browser=browser_type)

    yield page

    page.close()


@pytest.fixture
def herokuapp(browser_type):
    page = HerokuAppPage(browser=browser_type)

    yield page

    page.close()


# UI study2 fixtures -------------------------------------------------------------------------------------------------
@pytest.fixture
def google_cloud(request, browser_type):
    general_page = GeneralPage(browser=browser_type)
    general_page.go_to(general_page.CLOUD_URL)

    yield general_page

    screenshot_on_failure(request, general_page)
    general_page.close()


@pytest.fixture
def google_calc(request, browser_type):
    general_page = GeneralPage(browser=browser_type)
    general_page.go_to(general_page.CALC_URL)

    yield general_page

    screenshot_on_failure(request, general_page)
    general_page.close()


# HTML report configuration ------------------------------------------------------------------------------------------
# Maby broke the tests in Jenkins try to run without it
# def pytest_html_report_title(report):
#     report.title = "Testing project!"


# Screenshots on fail ------------------------------------------------------------------------------------------------
# also you need to add "screenshot_on_failure" method to the fixtures
def screenshot_on_failure(request, page):
    if request.node.rep_call.failed:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Screenshot name in generated report
        filename = f"failed_test_{timestamp}.png"
        screenshot = page.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=filename, attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep