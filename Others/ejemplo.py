import unittest

class PruebaCadenas(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('xopa'.upper(), 'XOPA')

    def test_isupper(self):
        self.assertTrue('XOPA'.isupper())
        self.assertFalse('Xopa'.isupper())

    def test_split(self):
        s = 'xopa gente'
        self.assertEqual(s.split(), ['xopa', 'gente'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
        unittest.main()

