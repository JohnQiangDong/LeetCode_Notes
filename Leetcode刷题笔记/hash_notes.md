

# 字典操作学习笔记

## 1. 使用 `defaultdict`

`defaultdict` 是 Python 的 `collections` 模块中的一个类，提供了一个默认值功能，当访问的键不存在时，不会抛出 `KeyError`，而是返回一个默认的值。这对于需要频繁处理默认值的情况非常有用，例如计数、分组等操作。

### 导入模块

```python
from collections import defaultdict
```

### 用法示例

```python
# 创建一个默认值为 int（即 0）的 defaultdict
dd = defaultdict(int)
dd['a'] += 1  # Output: {'a': 1}

# 创建一个默认值为 list 的 defaultdict
dd = defaultdict(list)
dd['a'].append(1)  # Output: {'a': [1]}

# 创建一个默认值为 set 的 defaultdict
dd = defaultdict(set)
dd['a'].add(1)  # Output: {'a': {1}}
```

- **`defaultdict(int)`**：创建一个默认值为 `0` 的字典，可以直接进行加法操作，非常适合用于计数。
- **`defaultdict(list)`**：创建一个默认值为空列表的字典，非常适合用于将多个值分组到一个键下。
- **`defaultdict(set)`**：创建一个默认值为空集合的字典，适合用于存储不重复的元素。

## 2. 创建字典

```python
# 创建空字典
my_dict = {}

# 通过键值对创建字典
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 使用 dict() 函数创建字典
my_dict = dict(name='Alice', age=25, city='New York')
```

## 3. 访问字典元素

```python
my_dict = {'name': 'Alice', 'age': 25}

# 通过键访问
name = my_dict['name']  # Output: 'Alice'

# 使用 get() 方法访问（如果键不存在，不会抛出错误，而是返回 None 或指定的默认值）
age = my_dict.get('age')  # Output: 25
gender = my_dict.get('gender', 'Female')  # Output: 'Female'
```

## 4. 修改字典

```python
my_dict = {'name': 'Alice', 'age': 25}

# 修改值
my_dict['age'] = 26

# 添加新键值对
my_dict['city'] = 'New York'
```

## 5. 删除字典元素

```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 使用 del 关键字删除键值对
del my_dict['age']

# 使用 pop() 方法删除键值对并返回其值
city = my_dict.pop('city')  # Output: 'New York'

# 使用 popitem() 方法删除并返回字典中的最后一个键值对（Python 3.7+）
last_item = my_dict.popitem()  # Output: ('name', 'Alice')

# 使用 clear() 方法清空字典
my_dict.clear()  # Output: {}
```

## 6. 字典常用方法

- **`keys()`**：返回字典中所有键的视图对象。

    ```python
    my_dict = {'name': 'Alice', 'age': 25}
    keys = my_dict.keys()  # Output: dict_keys(['name', 'age'])
    ```

- **`values()`**：返回字典中所有值的视图对象。

    ```python
    values = my_dict.values()  # Output: dict_values(['Alice', 25])
    ```

- **`items()`**：返回字典中所有键值对的视图对象。

    ```python
    items = my_dict.items()  # Output: dict_items([('name', 'Alice'), ('age', 25)])
    ```

- **`update()`**：使用另一个字典或键值对的迭代对象更新字典。

    ```python
    my_dict.update({'age': 26, 'city': 'New York'})
    ```

## 7. 字典的遍历

```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 遍历键
for key in my_dict:
    print(key)

# 遍历值
for value in my_dict.values():
    print(value)

# 遍历键值对
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## 8. 使用 `Counter`

`Counter` 是 `collections` 模块中的一个类，用于计数。

```python
from collections import Counter

# 创建一个 Counter 对象
counter = Counter('hello world')

# 计数结果
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 获取计数最多的两个元素
most_common = counter.most_common(2)  # Output: [('l', 3), ('o', 2)]
```

## 9. 使用 `OrderedDict`

`OrderedDict` 是 `collections` 模块中的一个类，在 Python 3.7+ 的版本中，普通字典本身也会保持插入顺序，因此 `OrderedDict` 的使用场景减少。

```python
from collections import OrderedDict

# 创建一个 OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# 迭代时保持插入顺序
# Output: ('a', 1), ('b', 2), ('c', 3)
```

## 10. 字典的集合操作

字典的键可以看作集合，因此可以使用集合操作来比较字典的键。

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

# 交集：字典中共同的键
common_keys = dict1.keys() & dict2.keys()  # Output: {'b', 'c'}

# 差集：dict1 中独有的键
unique_keys = dict1.keys() - dict2.keys()  # Output: {'a'}

# 对称差：两个字典中独有的键
symmetric_difference = dict1.keys() ^ dict2.keys()  # Output: {'a', 'd'}
```

## 11. 字典推导式

字典推导式用于根据现有字典生成一个新的字典。

```python
# 反转字典的键值对
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original_dict.items()}
# Output: {1: 'a', 2: 'b', 3: 'c'}
```