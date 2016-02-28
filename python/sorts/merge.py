import unittest

class MergeSort(list):

    def sort(self):
        if len(self) <= 1:
            return self

        left  = self.__class__()
        right = self.__class__()

        for idx, item in self:
            if idx % 2:  # odds to the left evens to the right
                left.append(item)
            else:
                right.append(item)

        left.sort()
        right.sort()

        self.merge(left, right)

        return self

    def merge(left, right):
        result = self.__class__()

        while left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())

        while left:
            result.append(left.popleft())

        while right:
            result.append(right.popleft())

        self = result

        return self


class TestMergeSort(unittest.TestCase):

    def test_mergesort_subclass(self):
        a = MergeSort([])
        assert isinstance(a, list)

    def test_sort_normal(self):
        a = MergeSort([41,35,12,34,56,2,3,23,94,4])
        b = [2,3,4,12,23,34,35,41,56,94]

        a.sort()

        self.assertEquals(a, b)


if __name__ == '__main__':
    print ("Testing\n")
    unittest.main()
