from unittest import TestCase


def swap(lst, a, b):
  lst[a], lst[b] = lst[b], lst[a]

def sort(lst, lo, hi):
  if lo < hi:
    p = split(lst, lo, hi)  # sort sweep
    sort(lst, lo, p - 1)  # left
    sort(lst, p + 1, hi)  # right

def split(lst, lo, hi):
  wall = lo
  pivot = lst[hi]

  for i in range(lo, hi):
    if lst[i] < pivot:
      swap(lst, i, wall)
      wall += 1

  swap(lst, wall, hi)

  return wall


class TestQsort(TestCase):

  def test_qsort_unsorted(self):
    a = [34,2,46,5,56,25,56,14]
    e = [2,5,14,25,34,46,56,56]

    b = list(a)

    sort(b, 0, len(b) - 1)

    self.assertEqual(b, e)





