import unittest

class UnitTest(unittest.TestCase):
  def test_divide(self):
    self.assertEqual(divide(9, 3), 3)
  
  def test_dividezero(self):
    with self.assertRaises(ZeroDivisionError):
      divide(9, 0)
      

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("На 0 делить нельзя")
  return x / y

if __name__ == "__main__":
  unittest.main()