from unittest import TestCase

class SelectionSort(list):

  def sort(self):
    
    sorted = []

    while self:
      sorted.append(self.pop(self._select()))

    self.extend(sorted)

    return self

  def _select(self):
    i, m = 0, self[0]
    for idx, ele in enumerate(self):
      if ele < m:
        i, m = idx, self[idx]

    return i

class TestSelectionSort(TestCase):

  def test_sort(self):
    a = SelectionSort([23, 42, 4, 16, 8, 15])
    b = [4, 8, 15, 16, 23, 42]

    a.sort()

    self.assertEqual(a, b)


