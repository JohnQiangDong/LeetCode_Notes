
# Queue 使用学习笔记



## 1. 使用 `deque` 实现 FIFO 队列

`deque` 默认作为双端队列使用，但我们可以用它实现先进先出的队列。

```python
from collections import deque

# 创建空队列
q = deque()

# 向队列尾部添加元素
q.append(10)
q.append(20)
q.append(30)

# 从队列头部移除元素
first_item = q.popleft()  # Output: 10
second_item = q.popleft()  # Output: 20
```

## 2. 使用 `deque` 实现 LIFO 队列（栈）

`deque` 也可以用于实现后进先出的队列，类似于栈结构。

```python
from collections import deque

# 创建空栈
stack = deque()

# 向栈顶添加元素
stack.append(10)
stack.append(20)
stack.append(30)

# 从栈顶移除元素
top_item = stack.pop()  # Output: 30
second_top_item = stack.pop()  # Output: 20
```


## 3. 常用操作

### 3.1 添加元素

- **`append()`**：向队列尾部或栈顶添加元素。

### 3.2 获取元素

- **`popleft()`**：从队列头部获取元素（FIFO队列）。
- **`pop()`**：从栈顶获取元素（LIFO队列）。

### 4.3 检查队列状态

- **`len(q)`**：返回队列的当前长度。
- **`not q`**：检查队列是否为空，若为空返回 `True`。

## 5. 使用场景

- **FIFO 队列**：任务调度、广度优先搜索（BFS）。
- **LIFO 队列（栈）**：深度优先搜索（DFS）、回溯算法。