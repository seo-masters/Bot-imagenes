import requests
import json


class PexelsAPI:
    def __init__(
        self, api_key="hpLJx9jyhSs0q5aN1mw73aS4JbxrNfgseKuvT4CD1gg4tFIkh9HMxLje"
    ):
        self.api_key = api_key
        self.api_url = "https://api.pexels.com/v1/"

    def search(self, query, per_page=2, page=1):
        headers = {
            "Authorization": self.api_key
        }

        try:
            response = requests.get(
                f"{self.api_url}/search?query={query}&per_page={per_page}&page={page}",
                headers=headers,
            )
            if response.status_code == 200:
                data = response.json()
                return True, data
            else:
                return False, "status_code " + str(response.status_code)
            
        except Exception  as e:
            print(f"Error: {e}")
            raise ValueError(f"Error: {e}")


class Photo:
    def __init__(self, data):
        self.id = data["id"]
        self.url = data["url"]
        self.alt = data["alt"]
