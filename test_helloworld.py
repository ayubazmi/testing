# test_helloworld.py
import unittest
from helloworld import say_hello

class TestHelloWorld(unittest.TestCase):

    def test_say_hello(self):
        result = say_hello()
        self.assertEqual(result, "Hello, World!")


if __name__ == '__main__':
    unittest.main()

