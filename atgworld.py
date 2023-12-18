import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):

    def test_website_connection(self):

        website_url = "https://atg.world"
        print("Starting the website connection test...")

        try:
            print(f"Sending a GET request to {website_url}")
            response = requests.get(website_url)

            print(f"Response status code: {response.status_code}")

            response.raise_for_status()
            print(f"Successfully connected to {website_url}")
            print(f"Test case pass")

            self.assertEqual(response.status_code, 200)

        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to {website_url}. Error: {e}")
            self.fail(f"Failed to connect to {website_url}. Error: {e}")

if __name__ == '__main__':
    unittest.main()


