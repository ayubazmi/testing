# test_helloworld.py
import unittest
from helloworld import say_hello

class TestHelloWorld(unittest.TestCase):

    def test_say_hello(self):
        result = say_hello()
        expected_result = "Hello, World!"

        if result == expected_result:
            print("Test case pass.")
        else:
            print(f"Test case fails. Expected '{expected_result}', but got '{result}'.")

if __name__ == '__main__':
    unittest.main()

