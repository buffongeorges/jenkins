from APP import frac
import unittest

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(frac(1, 2).mult(frac(2, 3)).a, 3)

        
if __name__ == '__main__':
    unittest.main()


