from unittest import TestCase

class Node:
  value = None
  parent = None
  right = None
  left = None

  def __init__(self, value):
    self.value = value

  @property
  def children(self):
    children = []
    if self.left:
      children.append(self.left)
    if self.right:
      children.append(self.right)

    return children

  @property
  def is_left(self):
    if self.parent and self.parent.left:
      if self.value == self.parent.left.value:
        return True

    return False

  @property
  def is_leaf(self):
    return len(self.children) == 0

  def delete_child(self, value):
    if self.left and self.left.value == value:
      self.left = None
      return self
    elif self.right and self.right.value == value:
      self.right = None
      return self

    return None

  def delete_from_parent(self):
    self.parent.delete_child(self.value)
    return self

  def _delete_single_parent(self):
    child = self.children[0]
    child.parent = self.parent

    if self.is_left:
      self.parent.left = child
    else:
      self.parent.right = child

    self.parent = None

  def delete(self):
    if self.is_leaf:
      self.delete_from_parent()
      return True
    elif len(self.children) == 1:
      self._delete_single_parent()
      return True
    elif len(self.children) == 2:
      n = self.right
      while not n.is_leaf:
        n = n.left

      self.value = n.value
      n.delete()
      return True

    return False

  def insert(self, node):
    if node.value < self.value:
      if self.left:
        self.left.insert(node)
      else:
        node.parent = self
        self.left = node
    elif node.value > self.value:
      if self.right:
        self.right.insert(node)
      else:
        node.parent = self
        self.right = node


  def find(self, search):
    if self.value == search:
      return self

    for child in self.children:
      n = child.find(search)
      if n:
        return n

    return None

class Tree:
  root = None

  def __init__(self, lst=[]):
    for n in lst:
      self.insert(n)

  def insert(self, value):
    n = Node(value)

    if not self.root:
      self.root = n
      return self.root 

    self.root.insert(n)
    return n

  def find(self, search):
    return self.root.find(search)

  def delete(self, value):
    n = self.root.find(value)
    if n:
      return n.delete()
    else:
      return False

class TestTree(TestCase):
  tree = None

  def setUp(self):
    self.tree = Tree()

  def tearDown(self):
    self.tree = None

  def test_root(self):
    self.tree.insert(5)
    self.assertEqual(self.tree.root.value, 5)

  def test_left_and_right(self):
    self.tree.insert(5)
    self.tree.insert(2)
    self.tree.insert(18)

    self.assertEqual(self.tree.root.left.value, 2)
    self.assertEqual(self.tree.root.right.value, 18)

  def test_structure(self):
    self.tree = Tree([5,2,18,-4,3])
    self.assertEqual(self.tree.root.value, 5)
    self.assertEqual(self.tree.root.left.value, 2)
    self.assertEqual(self.tree.root.left.left.value, -4)
    self.assertEqual(self.tree.root.left.left.parent.value, 2)
    self.assertEqual(self.tree.root.left.right.value, 3)
    self.assertEqual(self.tree.root.left.right.parent.value, 2)
    self.assertEqual(self.tree.root.right.value, 18)

  def test_find(self):
    self.tree = Tree([5,2,18,-4,3])
    n = self.tree.find(3)
    self.assertEqual(n.value, 3)
    self.assertTrue(n.is_leaf)

  def test_delete_leaf(self):
    self.tree = Tree([5,2,18,-4,3])
    self.assertEqual(self.tree.root.left.right.value, 3)
    self.assertTrue(self.tree.delete(3))
    self.assertIsNone(self.tree.root.left.right)

  def test_delete_single_parent(self):
    self.tree = Tree([5,2,18,-4,3,21,19,25])
    self.assertEqual(self.tree.root.right.value, 18)
    self.assertEqual(self.tree.root.right.right.value, 21)
    self.assertEqual(self.tree.root.right.right.left.value, 19)
    self.assertEqual(self.tree.root.right.right.right.value, 25)
    self.assertTrue(self.tree.delete(18))
    self.assertEqual(self.tree.root.right.value, 21)
    self.assertEqual(self.tree.root.right.left.value, 19)
    self.assertEqual(self.tree.root.right.right.value, 25)
