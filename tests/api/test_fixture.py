""" Here I learned how to use fixtures in tests """

import pytest


@pytest.mark.first_using_fixture
def test_remove_name(user):
    user.name = ""

    assert user.name == ""


@pytest.mark.first_using_fixture
def test_name(user):
    assert user.name == "Pavlo"


@pytest.mark.first_using_fixture
def test_second_name(user):
    assert user.second_name == "Lekhitskyi"
