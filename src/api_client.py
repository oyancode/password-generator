import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://random-word-api.herokuapp.com/word?number="

    def get_random_words(self, number):
        response = requests.get(self.base_url + str(number))
        if response.status_code == 200:
            return response.json()
        else:
            return None