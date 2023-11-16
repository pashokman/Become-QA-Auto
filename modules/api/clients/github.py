import requests


class GitHub():
    
    def get_user(self, username):
        response = requests.get(f"https://api.github.com/users/{username}")
        body = response.json()

        return body


    def search_repo(self, repo_name):
        response = requests.get("https://api.github.com/search/repositories", 
                                params={"q": repo_name})
        body = response.json()

        return body


    def get_emojis_list(self):
        response = requests.get("https://api.github.com/emojis")
        body = response.json()

        return body


    def get_commit_list(self):
        response = requests.get("https://api.github.com/repos/pashokman/Become-QA-Auto/commits")
        body = response.json()

        return body
