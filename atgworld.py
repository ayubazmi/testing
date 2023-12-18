import unittest
import requests


class TestWebsiteConnection(unittest.TestCase):

    def test_website_connection(self):
        # Define the website URL
        website_url = "https://atg.world"

        # Log step: Start of the test
        print("Starting the website connection test...")

        # Try to make a request to the website
        try:
            # Log step: Sending request to the website
            print(f"Sending a GET request to {website_url}")
            response = requests.get(website_url)

            # Log step: Checking response status code
            print(f"Response status code: {response.status_code}")

            response.raise_for_status()  # Raise HTTPError for bad responses

            # Log step: Website loaded successfully
            print(f"Successfully connected to {website_url}")
            print(f"Test case pass")

            self.assertEqual(response.status_code, 200)  # Check if the response status is 200 (OK)

        except requests.exceptions.RequestException as e:
            # Log step: Exception occurred, website didn't load
            print(f"Failed to connect to {website_url}. Error: {e}")
            self.fail(f"Failed to connect to {website_url}. Error: {e}")


if __name__ == '__main__':
    unittest.main()

