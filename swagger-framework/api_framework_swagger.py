from dataclasses import dataclass
import requests
from tenacity import retry, stop_after_attempt, wait_fixed


class BaseRequests:
    TIMEOUT = 10
    MAX_RETRIES = 10

    @retry(stop=stop_after_attempt(MAX_RETRIES), wait=wait_fixed(TIMEOUT))
    def prevent(api_request):
        """This method will be handling amount of API requests
        based on time to prevent DDoS attack"""
        pass


@dataclass
class RequestPOST(BaseRequests):

    @staticmethod
    def post_create_record(endpoint, payload):
        """This realization of POST method will return an ID of new created record"""

        response = requests.post(endpoint, json=payload)
        try:
            if response.status_code == 200:
                json_response = response.json()
                new_record_id = json_response["Id"]
                return int(new_record_id)

            else:
                print(f"POST request failed with status code {response.status_code}")

        except ValueError:
            print(f"Response content:\n{response.text}")
            return None


@dataclass
class RequestGET(BaseRequests):

    @staticmethod
    def get_record_data(endpoint, record_id):
        """This realization of GET method will return Name of the new created record"""

        headers = {"Id": {record_id}}
        response = requests.get(endpoint, headers)
        try:
            if response.status_code == 200:
                json_response = response.json()
                record_name = json_response["Name"]
                return str(record_name)

            else:
                print(f"GET request failed with status code {response.status_code}")

        except ValueError:
            print(f"Response content:\n{response.text}")
            return None


@dataclass
class RequestPUT(BaseRequests):

    @staticmethod
    def put_update_record(endpoint, payload):
        """This realization of PUT method will update the record name"""

        response = requests.put(endpoint, json=payload)
        try:
            if response.status_code == 200:
                json_data = response.json()
                updated_record_name = json_data["Name"]
                return updated_record_name

            else:
                print(f"PUT request failed with status code {response.status_code}")

        except ValueError:
            print(f"Response content:\n{response.text}")
            return None


@dataclass
class RequestDELETE(BaseRequests):

    @staticmethod
    def delete_record(endpoint, record_id):
        """This realization of DELETE method will delete the record"""

        endpoint = (
            f"{endpoint}/{record_id}?api_key=b856daf2-79be-d955-4261-5fc8845006f2"
        )
        response = requests.delete(endpoint)
        try:
            if response.status_code == 204:
                return response.status_code

            else:
                print(f"DELETE request failed with status code {response.status_code}")

        except ValueError:
            print(f"Response content:\n{response.text}")
            return None
