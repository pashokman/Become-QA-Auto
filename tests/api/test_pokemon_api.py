import pytest


@pytest.mark.pokemon_api
def test_pokemon_ditto_name(pokemon_api):
    pokemon = pokemon_api.get_pokemon("ditto")
    assert pokemon["forms"][0]["name"] == "ditto"


@pytest.mark.pokemon_api
def test_pokemon_ditto_base_experience(pokemon_api):
    pokemon = pokemon_api.get_pokemon("ditto")
    assert pokemon["base_experience"] == 101


@pytest.mark.pokemon_api
def test_pokemon_ditto_id(pokemon_api):
    pokemon = pokemon_api.get_pokemon("ditto")
    assert pokemon["id"] == 132


@pytest.mark.pokemon_api
def test_pokemon_ditto_type(pokemon_api):
    pokemon = pokemon_api.get_pokemon("ditto")
    assert pokemon["types"][0]["type"]["name"] == "normal"
