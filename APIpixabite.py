import requests
import os

class PixabayAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://pixabay.com/api/"

    def search(self, query):
        try:
            params = {
                "key": self.api_key,
                "q": query,
            }
            response = requests.get(self.api_url, params=params)

            if response.status_code == 200:
                data = response.json()
                return True, data
            else:
                return False, f"status_code {response.status_code}"

        except Exception as e:
            print(f"Error: {e}")
            raise ValueError(f"Error: {e}")

    def download_photos(self, query, download_folder="./photos"):
        success, data = self.search(query)
        if success:
            for hit in data.get("hits", []):
                image_url = hit["largeImageURL"]
                image_extension = image_url.split(".")[-1]
                image_filename = f"{hit['id']}.{image_extension}"
                image_path = os.path.join(download_folder, image_filename)

                try:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(image_path, "wb") as file:
                            file.write(response.content)
                        print(f"Descargada la imagen: {image_filename}")
                    else:
                        print(f"No se pudo descargar la imagen: {image_filename}, status_code {response.status_code}")
                except Exception as e:
                    print(f"Error al descargar la imagen: {image_filename}, Error: {e}")
