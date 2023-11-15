import pytest

# API modules-------------------------------------------
from modules.api.clients.github import GitHub
from modules.api.clients.pokemon import Pokemon
from modules.api.clients.restfool_booker import RestBooker

# Database module-------------------------------------------
from modules.common.database import Database

# UI pages modules-------------------------------------------
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.uakinoclub_page import UAKinoClubPage
from modules.ui.page_objects.herokuapp_page import HerokuAppPage


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


# API fixtures-------------------------------------------
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


# Databse fixtures-------------------------------------------
@pytest.fixture
def database():
    db = Database()

    yield db


# UI fixtures-------------------------------------------
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
