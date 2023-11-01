import pytest

from modules.api.clients.github import GitHub
from modules.api.clients.pokemon import Pokemon

from modules.common.database import Database

from selenium import webdriver
from selenium.webdriver.common.by import By


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
    