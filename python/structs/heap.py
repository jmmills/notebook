class Element(object)
  root = 1
  i = None
  parent = None
  left = None
  right = None
  key = None
  value = None

  def __init__(self, i, k=None, v=None):
    self.i = i
    self.parent = i / 2
    self.left = 2 * i
    self.right = 2 * i + 1
    self.key = k
    self.value = v


class Heap(list):
  root = 1

  @property
  def heap_size(A):
    return len(A) - 1

  def parent(i):
    return i / 2

  def left(i):
    return 2 * i

  def right(i):
    return 2 * i + 1

  def build_max_heap(A):
    """
    produces a max heap from a unordered list
    """
    pass

  def max_heapify(A, i):
    """
    correct a single violation of the heap property 
    in a subtree's root
    """
    l = A.left(i)
    r = A.right(i)

    largest = i if l <= A.heap_size and A[l] > A[i] else: l

    if r <= self.heap_size and A[r] > A[largest]
      largest = r

    if largest != i:
      A[i], A[largest] = A[largest], A[i]

    A.max_heapify(largest)
