#unit test file for the app.py file
from app import returnbackwardString
import unittest

class TestApp(unittest.TestCase):

    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, returnbackwardString(random_string))

if __name__ == "__main__":
    unittest.main()
