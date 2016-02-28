import unittest

class MergeSort(list):

    def sort(self):
        if len(self) <= 1:
            return self

        left  = self.__class__()
        right = self.__class__()

        for idx, item in enumerate(self):
            if idx % 2:  # odds to the left evens to the right
                left.append(item)
            else:
                right.append(item)

        left.sort()
        right.sort()

        self.merge(left, right)

        return self

    def merge(self, left, right):
        del self[:]

        while left and right:
            if left[0] <= right[0]:
                self.append(left.pop(0))
            else:
                self.append(right.pop(0))

        while left:
            self.append(left.pop(0))

        while right:
            self.append(right.pop(0))

        return self


class TestMergeSort(unittest.TestCase):

    def test_mergesort_subclass(self):
        a = MergeSort([])
        assert isinstance(a, list)

    def test_sort_normal(self):
        a = MergeSort([41,35,12,34,56,2,3,23,94,4])
        b = [2,3,4,12,23,34,35,41,56,94]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_duplicates(self):
        a = MergeSort([3, 3, 1, 5])
        b = [1, 3, 3, 5]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_single(self):
        a = MergeSort([3])
        b = [3]

        a.sort()

        self.assertEqual(a, b)

    def test_sort_empty(self):
        a = MergeSort([])
        b = []

        a.sort()

        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
