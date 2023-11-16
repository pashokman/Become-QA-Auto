import requests


class Pokemon():
    
    def get_pokemon(self, pokemon_name):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        body = response.json()

        return body
