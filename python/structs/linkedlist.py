from unittest import TestCase

class Node(object):
  value = None
  next_node = None
  prev_node = None

  def __init__(self, value):
    self.value = value

  def set_next(self, node):
    self.next_node = node
    return self

  def search(self, value):
    if self.value == value:
      return self
    elif self.next_node:
      return self.next_node.search(value)
    else:
      return None


class LinkedList(object):

  def __init__(self, head=None):
    self.head = head

  def insert(self, value):
    n = Node(value)
    n.set_next(self.head)
    self.head = n
    return n

  @property
  def size(self):
    n = self.head
    s = 0

    while n:
      s += 1
      n = n.next_node
  
    return s

  def search(self, value):
    r = self.head.search(value)
    
    if r:
      return r
    else:
      raise ValueError("Not found")

  def delete(self, value):
    current = self.head
    previous = None
    found = False

    while current and not found:
      if current.value == value:
        found = True
      else:
        previous = current
        current = current.next_node
    
    if not current and not found:
      raise ValueError("Not found")

    if previous and current.next_node:
      previous.set_next(current.next_node)
      del current
      return True

    if not previous:
      self.head = current.next_node
      return True



class TestLinkedList(TestCase):

  def make_list(self):
    return LinkedList()

  def populate_list(self):
    for i in range(0, 10):
      self.linkedlist.insert(i)

  def setUp(self):
    self.linkedlist = self.make_list()

  def tearDown(self):
    self.linkedlist = None

  def test_insert(self):
    a = self.linkedlist.insert('a')
    self.assertIsInstance(a, Node)
    self.assertEqual(a.value, 'a')
    self.assertEqual(self.linkedlist.head.value, 'a')

  def test_size(self):
    self.populate_list()
    self.assertEqual(self.linkedlist.size, 10)

  def test_search_found(self):
    self.populate_list()
    n = self.linkedlist.search(5)
    self.assertEqual(n.value, 5)

  def test_search_notfound(self):
    self.populate_list()
    with self.assertRaises(ValueError):
      self.linkedlist.search(11)

  def test_delete_middle(self):
    self.populate_list()
    o = self.linkedlist.head
    self.assertTrue(self.linkedlist.delete(5))
    self.assertEqual(self.linkedlist.size, 9)
    self.assertIs(self.linkedlist.head, o)
    
  def test_delete_end(self):
    self.populate_list()
    self.assertTrue(self.linkedlist.delete(9))
    self.assertEqual(self.linkedlist.size, 9)
    self.assertEqual(self.linkedlist.head.value, 8)

  def test_delete_toempty(self):
    self.assertTrue(self.linkedlist.insert('a'))
    self.assertEqual(self.linkedlist.size, 1)
    self.assertTrue(self.linkedlist.delete('a'))
    self.assertEqual(self.linkedlist.head, None)
    self.assertEqual(self.linkedlist.size, 0)

  def test_delete_notfound(self):
    with self.assertRaises(ValueError):
      self.linkedlist.delete('a')
