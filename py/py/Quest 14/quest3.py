import unittest

class UnitTest(unittest.TestCase):
  def setUp(self):
    self.calc = Calculator()
    
  def test_add(self):
    self.assertEqual(self.calc.add(5, -5), 0)
  def test_rem(self):
    self.assertEqual(self.calc.rem(53, 21), 32)
  def test_div(self):
    self.assertAlmostEqual(self.calc.div(63, 22), 3, delta=0.2)
  def test_div_zero(self):
    with self.assertRaises(ZeroDivisionError):
      self.calc.div(1, 0)
  def test_mult(self):
    self.assertEqual(self.calc.mult(10, 55), 550)

class Calculator():
  def add(self, x, y):
    return x + y
  def rem(self, x, y):
    return x - y
  def div(self, x, y):
    if y == 0:
      raise ZeroDivisionError("На 0 делить нельзя")
    return x / y
  def mult(self, x, y):
    return x * y
  

if __name__ == "__main__":
  unittest.main()