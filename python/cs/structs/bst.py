from unittest import TestCase

class Node:
  def __init__(self, key, value=None),
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  @property
  def is_leaf(self):
    if not (self.left and self.right)

  def insert(self, node):
    #  if this node is a leaf insert new nodes to the left
    if self.is_leaf:
      return self.left = node

    #  if new nodes greater is less than ours assign it to the left
    #  if there is already a left node recurse into it's insert method
    if node.key < self.key:
      if self.left:
        return self.left.insert(node)
      else:
        return self.left = node

    #  if new nodes greater is greater than ours assign it to the right
    #  if there already a right node recurse into it's insert method
    if node.key > self.key:
      if self.right:
        return self.right.insert(node)
      else:
        return self.right = node

    # if we have reached here it means that the new node's key is equal to ours
    # as a BST has distinct key values, return false since we didn't insert it
    return False

  def search(self, key):
    # if this is the key we are looking for return it
    if self.key == key:
      return self
    else:
      # if we aren't a leaf (no-children) then recurse into child nodes for search
      # left < key < right
      if not self.is_leaf:
        if key < self.key:
          return self.left.search(key)

        if key > self.key:
          return self.right.search(key)
      else:
        return False

class Tree:

  def __init__(self):
    self.root = None

  def insert(self, key, value):
    n = Node(key, value)
    
    if not self.root:
      self.root = n
    else:
      self.root.insert(n)

    return n

  def search(self, key):
    return self.root.search(key)

  def delete(self, key):  # dark magic!
    pass

  
