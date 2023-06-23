
from typing import List, Tuple


class WeatherDatabase:
    def __init__(self):
        """
        Initialize a new WeatherDatabase instance.
        """
        pass

    def save_request_data(self, city_name: str, request_time: str) -> None:
        """
        Save request data for a city to the database.

        Args:
        - city_name (str): The name of the city to save request data for.
        - request_time (str): The time the request was made, in ISO format.

        Returns:
        - None
        """
        pass

    def save_response_data(self, city_name: str, response_data: dict) -> None:
        """
        Save response data for a city to the database.

        Args:
        - city_name (str): The name of the city to save response data for.
        - response_data (dict): A dictionary containing weather information for the city, including temperature, feels like temperature, and last updated time.

        Returns:
        - None
        """
        pass

    def get_request_count(self) -> int:
        """
        Get the total number of requests made to the server.

        Returns:
        - int: The total number of requests made to the server.
        """
        pass

    def get_successful_request_count(self) -> int:
        """
        Get the total number of successful requests made to the server.

        Returns:
        - int: The total number of successful requests made to the server.
        """
        pass

    def get_last_hour_requests(self) -> List[Tuple[str, str]]:
        """
        Get a list of requests made in the last hour.

        Returns:
        - List[Tuple[str, str]]: A list of tuples containing the name of the city and the time the request was made, in ISO format.
        """
        pass

    def get_city_request_count(self) -> List[Tuple[str, int]]:
        """
        Get a count of requests made for each city.

        Returns:
        - List[Tuple[str, int]]: A list of tuples containing the name of the city and the number of requests made for that city.
        """
        pass

