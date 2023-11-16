import requests
from logging import getLogger

logger = getLogger(__name__)
logger.setLevel("INFO")

class MatrixApiClient:
    def __init__(self, homeserver_url, access_token):
        self.homeserver_url = homeserver_url
        self.access_token = access_token

    def get_calculated_matrix_distance(self, origin, destination):
        try:
            logger.info(f"Request: {self.homeserver_url}/maps/api/distancematrix/json"
                f"?key={self.access_token}"
                f"&origins={origin}"
                f"&destinations={destination}")
            
            response = requests.get(
                f"{self.homeserver_url}/maps/api/distancematrix/json"
                f"?key={self.access_token}"
                f"&origins={origin}"
                f"&destinations={destination}"
            )
        except Exception as e:
            logger.error(f"Error: {e}")
            raise e
        else:
            if response.status_code == 200:
                logger.info(f"Response: {response.json()}")
                return response.json()
            else:
                logger.error(f"Error: {response.status_code}")
                raise Exception(f"Error: {response.status_code}")
