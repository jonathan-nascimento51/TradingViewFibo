import unittest, re

class TestFeatures(unittest.TestCase):
    def test_functions_present(self):
        with open('fiboFractais.pine') as f:
            data = f.read()
        self.assertIn('getStrongestSwing', data)
        self.assertIn('hasImpulseBreakout', data)
        self.assertIn('topNMode', data)
        self.assertIn('Ignorado por TopN', data)

if __name__ == '__main__':
    unittest.main()
