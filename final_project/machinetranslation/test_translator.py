import unittest

import translator

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench("Hello, how are you?"), "Bonjour, comment es-tu?")
        self.assertNotEqual(translator.englishToFrench("I'm fine"), "I'm fine")
    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish("Je vais bien"), "I'm fine")
        self.assertNotEqual(translator.frenchToEnglish("Bonjour, comment es-tu?"), "Bonjour, comment es-tu?")

if __name__ == "__main__":
    unittest.main()