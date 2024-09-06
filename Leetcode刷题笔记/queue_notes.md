# Queue 模块操作学习笔记

## 1. 导入 `queue` 模块

```python
import queue
```

Python 的 `queue` 模块提供了多种线程安全的队列类型，用于在生产者和消费者之间传递数据，常见的队列类型包括 `Queue`、`LifoQueue` 和 `PriorityQueue`。

### 1.1 `Queue`

`Queue` 是一个FIFO（先进先出）的队列，数据按插入顺序读取。

```python
q = queue.Queue()

# 向队列中添加元素
q.put(10)
q.put(20)
q.put(30)

# 从队列中获取元素
first_item = q.get()  # Output: 10
second_item = q.get()  # Output: 20
```

### 1.2 `LifoQueue`

`LifoQueue` 是一个LIFO（后进先出）的队列，类似于栈，最后插入的元素最先被读取。

```python
lq = queue.LifoQueue()

# 向队列中添加元素
lq.put(10)
lq.put(20)
lq.put(30)

# 从队列中获取元素
last_item = lq.get()  # Output: 30
second_last_item = lq.get()  # Output: 20
```

### 1.3 `PriorityQueue`

`PriorityQueue` 是一个优先级队列，元素按照优先级从小到大进行排序，优先级较小的元素先出队。

```python
pq = queue.PriorityQueue()

# 添加元素，格式为 (优先级, 数据)
pq.put((2, "medium priority"))
pq.put((1, "high priority"))
pq.put((3, "low priority"))

# 从队列中获取元素，优先级小的先出
highest_priority_item = pq.get()  # Output: (1, "high priority")
```

## 2. 常用方法

### 2.1 `put(item, block=True, timeout=None)`

将元素 `item` 放入队列中。

- **参数**：
  - `block`：是否阻塞（默认 `True`，队列满时等待）
  - `timeout`：可选参数，表示在等待时长内如果队列满，则抛出 `Full` 异常

```python
q.put(10)  # 阻塞方式添加
q.put(20, block=False)  # 非阻塞方式添加，队列满时会抛出 queue.Full 异常
```

### 2.2 `get(block=True, timeout=None)`

从队列中取出元素。

- **参数**：
  - `block`：是否阻塞（默认 `True`，队列空时等待）
  - `timeout`：可选参数，表示在等待时长内如果队列为空，则抛出 `Empty` 异常

```python
item = q.get()  # 阻塞方式获取
item = q.get(block=False)  # 非阻塞方式获取，队列空时会抛出 queue.Empty 异常
```

### 2.3 `qsize()`

返回队列的当前大小。

```python
size = q.qsize()  # 获取队列大小
```

### 2.4 `empty()`

检查队列是否为空。

```python
is_empty = q.empty()  # 如果队列为空，返回 True
```

### 2.5 `full()`

检查队列是否已满（适用于初始化时设置最大容量的队列）。

```python
is_full = q.full()  # 如果队列满了，返回 True
```

## 3. 使用场景

- **FIFO 队列（`Queue`）**：用于任务调度，生产者和消费者模式。
- **LIFO 队列（`LifoQueue`）**：适合使用栈结构的场景，如回溯算法。
- **优先级队列（`PriorityQueue`）**：适用于需要根据优先级调度任务的场景。
