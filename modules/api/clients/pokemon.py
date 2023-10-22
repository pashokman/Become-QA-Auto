import requests


class Pokemon:
    def get_pokemon(self, pokemon_name):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        body = r.json()

        return body
