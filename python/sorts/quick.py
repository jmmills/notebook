import unittest

class QuickSort(list):

  def sort(self, start=0, stop=None):
    if stop is None:
      stop = len(self) - 1

    if stop - start > 0:
      pivot, left, right = self[start], start, stop

      while left <= right:
        while self[left] < pivot:
          left += 1
        while self[right] > pivot:
          right -= 1
        if left <= right:
          self[left], self[right] = self[right], self[left]
          left += 1
          right -= 1

      self.sort(start, right)
      self.sort(left, stop)

    return self



class TestQuickSort(unittest.TestCase):

    def test_quicksort_subclass(self):
        a = QuickSort([])
        assert isinstance(a, list)

    def test_sort_normal(self):
        a = QuickSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        b = [17, 20, 26, 31, 44, 54, 55, 77, 93]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_duplicates(self):
        a = QuickSort([3, 3, 1, 5])
        b = [1, 3, 3, 5]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_single(self):
        a = QuickSort([3])
        b = [3]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_empty(self):
        a = QuickSort([])
        b = []

        a.sort()

        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()

