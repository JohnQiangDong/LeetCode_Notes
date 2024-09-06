

# 二叉树学习笔记

## 1. LeetCode相关题目及其实现

### 1.1 [Binary Tree Inorder Traversal (94)](https://leetcode.com/problems/binary-tree-inorder-traversal/)

**题目要求**：实现二叉树的中序遍历。

**Python 实现**：

```python
def inorder_traversal(root):
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    
    return result
```

### 1.2 [Binary Tree Level Order Traversal (102)](https://leetcode.com/problems/binary-tree-level-order-traversal/)

**题目要求**：实现二叉树的层序遍历。

**Python 实现**：

```python
from collections import deque

def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### 1.3 [Maximum Depth of Binary Tree (104)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**题目要求**：计算二叉树的最大深度。

**Python 实现**：

```python
def max_depth(root):
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1
```

### 1.4 [Same Tree (100)](https://leetcode.com/problems/same-tree/)

**题目要求**：判断两棵二叉树是否相同。

**Python 实现**：

```python
def is_same_tree(p, q):
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

### 1.5 [Symmetric Tree (101)](https://leetcode.com/problems/symmetric-tree/)

**题目要求**：判断一棵二叉树是否对称。

**Python 实现**：

```python
def is_symmetric(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)
```

### 1.6 [Path Sum (112)](https://leetcode.com/problems/path-sum/)

**题目要求**：判断二叉树中是否存在一条从根到叶子的路径，其节点值之和等于目标和。

**Python 实现**：

```python
def has_path_sum(root, target_sum):
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        return root.val == target_sum
    
    target_sum -= root.val
    
    return has_path_sum(root.left, target_sum) or has_path_sum(root.right, target_sum)
```

### 1.7 [Invert Binary Tree (226)](https://leetcode.com/problems/invert-binary-tree/)

**题目要求**：翻转一棵二叉树。

**Python 实现**：

```python
def invert_tree(root):
    if root is None:
        return None
    
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    
    root.left = right
    root.right = left
    
    return root
```

### 1.8 [Serialize and Deserialize Binary Tree (297)](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

**题目要求**：实现二叉树的序列化和反序列化。

**Python 实现**：

```python
def serialize(root):
    def helper(node):
        if node is None:
            vals.append("#")
            return
        vals.append(str(node.val))
        helper(node.left)
        helper(node.right)
    
    vals = []
    helper(root)
    return " ".join(vals)

def deserialize(data):
    def helper():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    
    vals = iter(data.split())
    return helper()
```

## 2. 二叉树遍历方法

### 2.1 深度优先遍历（DFS）

#### 前序遍历（Pre-order Traversal）

```python
def preorder_traversal(root):
    if root is None:
        return []
    
    result = []
    result.append(root.val)
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    
    return result
```

#### 中序遍历（In-order Traversal）

```python
def inorder_traversal(root):
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    
    return result
```

#### 后序遍历（Post-order Traversal）

```python
def postorder_traversal(root):
    if root is None:
        return []
    
    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    
    return result
```

### 2.2 广度优先遍历（BFS）

#### 层序遍历（Level-order Traversal）

```python
from collections import deque

def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 3. 其他进阶操作

### 3.1 二叉树的直径

**题目要求**：计算二叉树的直径。

```python
def diameter_of_binary_tree(root):
    def depth(node):
        if node is None:
            return 0
        
        left = depth(node.left)
        right = depth(node.right)
        
        self.diameter = max(self.diameter, left + right)
        
        return max(left, right) + 1

    self.diameter = 0
    depth(root)
    return self.diameter
```

### 3.2 二叉树的最小深度

**题目要求**：计算二叉树的最小深度。

```python
def min_depth(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return min_depth(root.right) + 1
    
    if root.right is None:
        return min_depth(root.left) + 1
    
    return min(min_depth(root.left), min_depth(root.right)) + 1
```

