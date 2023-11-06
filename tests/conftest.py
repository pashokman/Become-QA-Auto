import pytest

from modules.api.clients.github import GitHub
from modules.api.clients.pokemon import Pokemon
from modules.api.clients.restfool_booker import Restbooker

from modules.common.database import Database

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


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def pokemon_api():
    api = Pokemon()

    yield api


@pytest.fixture
def database():
    db = Database()

    yield db
    

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

@pytest.fixture
def restbooker():
    api = Restbooker()

    yield api