import unittest

class UnitTest(unittest.TestCase):
  def test_add_natural(self):
    self.assertEqual(add(5, 4), 9)
  def test_add_zero(self):
    self.assertEqual(add(-1, 0), -1)
  def test_add_minus(self):
    self.assertEqual(add(-3, -4), -7)
  def test_add_mix(self):
    self.assertEqual(add(0, -4), -4)

def add(x, y):
  return x + y

if __name__ == "__main__":
  unittest.main()