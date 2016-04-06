from unittest import TestCase

def search(lst, value):
  for idx, v in enumerate(lst):
    if value == v:
      return idx

  return False

class Test(TestCase):
  a = []

  def setUp(self):
    self.a = [23,4,3,5,1,4,8]

  def tearDown(self):
    self.a = []

  def test_search_true(self):
    self.assertEqual(search(self.a, 4), 1)
    self.assertEqual(search(self.a, 5), 3)

  def test_search_false(self):
    self.assertFalse(search(self.a, 100))

  def test_bench_mark(self):
    for n in range(0, 2 ** 20):
      self.assertEqual(search(self.a, 4), 1)
