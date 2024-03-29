import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("*#" * 30)
        print("Class 2 -> class level setUp")
        print("*#" * 30)

    def test_class2_methodA(self):
        print("Running class 2 -> method A")

    def test_class2_methodB(self):
        print("Running class 2 -> method B")

    @classmethod
    def tearDownClass(self):
        print("*#" * 30)
        print("Class 2 -> class level tearDown")
        print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)