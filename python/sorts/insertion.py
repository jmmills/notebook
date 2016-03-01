from unittest import TestCase

class InsertionSort(list):

  def sort(self):
    for j, item in enumerate(self):
      while j > 0 and self[j - 1] > item:
        self[j] = self[j - 1]
        j -= 1

      self[j] = item

    return self

      
class TestInsertionSort(TestCase):

  def test_sort(self):
    a = InsertionSort([23, 42, 4, 16, 8, 15])
    b = [4, 8, 15, 16, 23, 42]

    a.sort()

    self.assertEqual(a, b)
