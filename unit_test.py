import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('maryville'.upper(), 'MARYVILLE')

    def test_isupper(self):
        self.assertTrue('MARYVILLE'.isupper())
        self.assertFalse('Marryville'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(), ['Hello', 'World'])

if __name__ == '__main__':
    unittest.main()