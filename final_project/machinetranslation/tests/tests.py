import unittest

from translator import english_to_french, french_to_english

class E2F(unittest.TestCase):

    def test1(self):
        """
        test null input for english_to_french
        """
        self.assertEqual(english_to_french(""), None)

    def test2(self):
        """
        test english to french translation using assertNotEqual()
        """
        self.assertNotEqual(english_to_french("Hello"), "Hello")

    def test3(self):
        """
        test english to french translation using assertEqual()
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class F2E(unittest.TestCase):
    def test1(self):
        """
        test null input for french_to_english
        """
        self.assertEqual(french_to_english(""), None)
    
    def test2(self):
        """
        test french to english translation using assertNotEqual()
        """
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

    def test3(self):
        """
        test french to english translation using assertEqual()
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
