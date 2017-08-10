from Functions import add
import unittest

class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5,add(2,3))
   

if __name__ == '__main__':
    unittest.main(exit=False)