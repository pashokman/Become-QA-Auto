""" All tests makes on pokemon - ditto, using fixture to get it's info. """

import pytest


@pytest.mark.pokemon_api
def test_pokemon_first_form_name(pokemon_api):
    assert pokemon_api["forms"][0]["name"] == "ditto", "Pokemon name is not 'ditto'"


@pytest.mark.pokemon_api
def test_pokemon_base_experience(pokemon_api):
    assert pokemon_api["base_experience"] == 101, "Pokemon base experience is not equal to 101"


@pytest.mark.pokemon_api
def test_pokemon_id(pokemon_api):
    assert pokemon_api["id"] == 132, "Pokemon id is not equal to 132"


@pytest.mark.pokemon_api
def test_pokemon_first_type_name(pokemon_api):
    assert pokemon_api["types"][0]["type"]["name"] == "normal", "Pokemon first type name is not equal to 'normal'"
