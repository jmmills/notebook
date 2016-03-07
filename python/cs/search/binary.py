from unittest import TestCase

def search(lst, value):  # assumes ordered list
  if len(lst) <= 1:
    return False

  mid = len(lst) // 2

  if lst[mid] == value:
    return True

  if lst[mid] < value:
    return search(lst[mid:], value)

  if lst[mid] > value:
    return search(lst[:mid], value)

  return False


class Test(TestCase):
  a = []

  def setUp(self):
    self.a = [1,3,4,4,5,8,23]

  def tearDown(self):
    self.a = []

  def test_search_true(self):
    self.assertTrue(search(self.a, 4))
    self.assertTrue(search(self.a, 5))

  def test_search_false(self):
    self.assertFalse(search(self.a, 100))

  def test_bench_mark(self):
    for n in range(0, 2 ** 20):
      self.assertTrue(search(self.a, 4))

