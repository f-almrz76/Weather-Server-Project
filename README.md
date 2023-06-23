# Weather Server Project 👨‍💻

## Introduction 🌤️

Welcome to the Weather Server Project! 🎉 This project is designed to help you practice your Python skills by creating a simple weather server that retrieves weather data from an external API and displays it to clients. 

👉🏼 Your task is to implement the server and client commands and store data in a database.

## Instructions 📝

### 1. Run the server 🚀

To run the server, open a command line window and navigate to the project directory. Then, execute the following command:

```sh 
python weather_server.py
```

👉🏼 10 points

### 2. Run the client command-line interface 💻

In a separate command line window, navigate to the project directory and run the following command to start the client:

```sh
python weather_client.py 
```

👉🏼 10 points

### 3. Enter a city name 🏙️

Once the client is running, you will be prompted to enter a city name. Type the name of a city and press Enter to request weather data from the server:

```
Enter a city name: San Francisco
```

👉🏼 10 points

### 4. Display weather data ☀️

If the city name is valid, the weather information will be displayed on the command line, like this:

```
Temperature: 18.5°C  
Feels like: 16.3°C
Last updated: 2023-06-22 15:40:00
```

👉🏼 10 points

### 5. Retry for an incorrect or invalid city name 🔄

If the city name entered is incorrect or invalid, an error message will be displayed. You can retry by entering a new city name:

```
Enter a city name: Invalid City
Error retrieving weather data: No matching location found.  
Enter a new city name: San Francisco  
```

👉🏼 10 points

### 6. Unit Testing 🧪

Add some unit tests for the `get_city_weather` method.

👉🏼 20 points

### 7. Entity Relationship Diagram (ERD) 🗂️

Create an ERD to store request and response data in two tables.

👉🏼 10 points

### 8. Additional Methods 📊

Add the following methods to get:

- Count of request
- Count of successful requests
- Last hour requests
- Each city request count

👉🏼 10 points

### 9. Store Data in a Database 💾

Store the request and response data in a database based on your ERD.

👉🏼 10 points

### 10. Database Unit Testing 🧪

Add unit tests for your database methods.

👉🏼 10 points

## Sample Output 📄

Here is a sample output of the completed project:

```
Enter a city name: San Francisco
Temperature: 18.5°C  
Feels like: 16.3°C
Last updated: 2023-06-22 15:40:00 

Enter a city name: Invalid City  
Error retrieving weather data: No matching location found.
    
Request count: 2
Successful request count: 1
Last hour requests: 
[('San Francisco', '2022-01-01 12:00:00'), ('Invalid City', '2022-01-01 12:15:00')]
City request counts: 
[('San Francisco', 1), ('Invalid City', 1)]
```

👉🏼 10 points

### Folder Structure
```
weather_project/
├── weather_server.py
├── weather_client.py
├── database.py
├── erd.png
├── requirements.txt
└── tests/
    ├── test_get_city_weather.py
    └── test_database.py
```

### Function Definition
#### weather_server.py
```python
def get_city_weather(city_name: str) -> dict:
    """
    Retrieve weather data from an external API for a given city.

    Args:
    - city_name (str): The name of the city to retrieve weather data for.

    Returns:
    - dict: A dictionary containing weather information for the city, including temperature, feels like temperature, and last updated time.
    """
    pass

def start_server() -> None:
    """
    Start the weather server.
    """
    pass
```

#### weather_client.py
```python
def start_client() -> None:
    """
    Start the weather client command-line interface.
    """
    pass
```

#### database.py
```python
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
```
