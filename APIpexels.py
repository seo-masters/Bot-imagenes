import requests
import os

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
            
        except Exception as e:
            print(f"Error: {e}")
            raise ValueError(f"Error: {e}")

    def download_photos(self, query, per_page=2, page=1, download_folder="./photos"):
        success, data = self.search(query, per_page, page)
        if success:
            for photo in data.get("photos", []):
                photo_id = photo["id"]
                photo_url = photo["src"]["original"]
                photo_extension = photo_url.split(".")[-1]
                photo_filename = f"{photo_id}.{photo_extension}"
                photo_path = os.path.join(download_folder, photo_filename)

                try:
                    response = requests.get(photo_url)
                    if response.status_code == 200:
                        with open(photo_path, "wb") as file:
                            file.write(response.content)
                        print(f"Descargada la foto: {photo_filename}")
                    else:
                        print(f"No se pudo descargar la foto: {photo_filename}, status_code {response.status_code}")
                except Exception as e:
                    print(f"Error al descargar la foto: {photo_filename}, Error: {e}")
