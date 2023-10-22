import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, repo_name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params={"q": repo_name}
        )
        body = r.json()

        return body

    def get_emojis_list(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    def get_commit_list(self):
        r = requests.get("https://api.github.com/repos/pashokman/Become-QA-Auto/commits")
        body = r.json()

        return body
