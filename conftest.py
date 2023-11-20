import pytest

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
@pytest.fixture
def sign_in_page():
    page = SignInPage()

    yield page

    page.close()


@pytest.fixture
def uakinoclub():
    page = UAKinoClubPage()

    yield page

    page.close()


@pytest.fixture
def herokuapp():
    page = HerokuAppPage()

    yield page

    page.close()


# UI study2 fixtures -------------------------------------------------------------------------------------------------
@pytest.fixture()
def google_cloud():
    general_page = GeneralPage()
    general_page.go_to(general_page.CLOUD_URL)

    yield general_page

    general_page.close()


@pytest.fixture()
def google_calc():
    general_page = GeneralPage()
    general_page.go_to(general_page.CALC_URL)
    general_page.fill_the_calc_form(4,'free','n1','CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8',
                                    'NVIDIA_TESLA_V100','1','2','europe-west3','1')

    yield general_page

    general_page.close()
