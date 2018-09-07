class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    current = self
    while current is not None:
      if current.left is None:
        current.cb(current.value)
        current = current.right
      else:
        pre = current.left
        while(pre.right is not None and pre.right != current):
          pre = pre.right
          if pre.right is None:
            pre.right = current
            current = current.left
          else: 
            pre.right = None
            current.cb(current.value)
            current = current.right

  def breadth_first_for_each(self, cb):
    current = self[0]
    current.cb()
    if current.left:
      current = current.left
      current.cb()
    else:
      current = current.right
      current.cb()


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
