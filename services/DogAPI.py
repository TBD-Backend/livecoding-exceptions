import requests


class DogAPIError(Exception):
    pass


class DogAPI:
    base_url = "http://dog-api.kinduff.com"

    def get_facts(self, number=1):

        response = None

        try:
            response = requests.get(f"{self.base_url}/api/facts?number={number}")
        except:
            raise DogAPIError("There was an error contacting the API")

        return response.json()


dog_api = DogAPI()
