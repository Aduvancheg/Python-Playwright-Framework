import os
from dataclasses import dataclass


@dataclass
class SecretKey:
    base_url_secret_key: str = os.getenv("API_URL_SECRET_KEY")

    @staticmethod
    def get_secret_key(session):
        """This method returns secret_key for accessing API of the swagger"""

        page = session
        try:
            page.goto(SecretKey.base_url_secret_key)
            page.get_by_role("button", name="Generate New Key").click()
            secret_key = page.locator("#key").inner_text()
            if secret_key:
                return secret_key
            else:
                raise Exception("secret_key element not found on the page")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            page.close()


class BasePage:
    base_url_coffee: str = os.getenv("API_URL_COFFEE")
    base_url_shope: str = os.getenv("API_URL_SHOP")

    # Version 2
    base_url_coffee2: str = os.environ["API_URL_COFFEE"]
    base_url_shope2: str = os.environ["API_URL_SHOP"]
    base_endpoint: str = None

    @staticmethod
    def endpoint_coffee(base_endpoint):
        """This method returns URL for API requests to coffee of swagger"""

        if base_endpoint:
            return f"{BasePage.base_url_coffee}{base_endpoint}"
        else:
            return NotImplementedError("Not emplemented yet")

    @staticmethod
    def endpoint_shop(base_endpoint):
        """This method returns URL for API requests to shop of swagger"""

        if base_endpoint:
            return f"{BasePage.base_url_shope}{base_endpoint}"
        else:
            return NotImplementedError("Not emplemented yet")


@dataclass
class ScreenShot:

    @staticmethod
    def take_screenshot(session):
        page = session
        page.screenshot(
            type="jpeg",
            path="/home/nikolay/projects/swagger-api-framework/swagger-framework/sample.jpg",
        )
