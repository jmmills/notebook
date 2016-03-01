from unittest import TestCase

class SelectionSort(list):

  def sort(self):
     
    for i in range(0, len(self)):
      min = i
      for j in range(i + 1, len(self)):
        if self[j] < self[min]:
          min = j
      if min != i:
        self[min], self[i] = self[i], self[min]


    return self

class TestSelectionSort(TestCase):

  def test_sort(self):
    a = SelectionSort([23, 42, 4, 16, 8, 15])
    b = [4, 8, 15, 16, 23, 42]

    a.sort()

    self.assertEqual(a, b)


