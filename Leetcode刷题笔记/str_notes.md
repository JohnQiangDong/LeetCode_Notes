

# 字符串操作学习笔记

## 相关LeetCode题目

1. [Longest Common Prefix (14)](https://leetcode.com/problems/longest-common-prefix/)
2. [Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/)
3. [Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/)
4. [Longest Palindromic Substring (5)](https://leetcode.com/problems/longest-palindromic-substring/)
5. [Reverse Words in a String (151)](https://leetcode.com/problems/reverse-words-in-a-string/)
6. [Implement strStr() (28)](https://leetcode.com/problems/implement-strstr/)

## 字符串方法总结

### 1. `split()`

**功能**：将字符串根据指定的分隔符分割成一个列表。

```python
text = "Hello, world!"
result = text.split(", ")
# Output: ['Hello', 'world!']
```

- **默认分隔符**：空格（包括多个空格、换行符等）
- **自定义分隔符**：可以传入任意字符或字符串作为分隔符

### 2. `join()`

**功能**：将列表中的元素连接成一个字符串，使用指定的分隔符。

```python
words = ["Hello", "world"]
result = " ".join(words)
# Output: "Hello world"
```

- **用法**：分隔符作为调用对象，列表作为参数

### 3. `strip()`, `lstrip()`, `rstrip()`

**功能**：移除字符串两端（或指定一侧）的空白字符或指定字符。

```python
text = "  Hello, world!  "
result = text.strip()
# Output: "Hello, world!"
```

- **`strip()`**：移除两端的空白字符
- **`lstrip()`**：移除左侧的空白字符
- **`rstrip()`**：移除右侧的空白字符

### 4. `replace()`

**功能**：将字符串中的指定子字符串替换为另一个子字符串。

```python
text = "Hello, world!"
result = text.replace("world", "Python")
# Output: "Hello, Python!"
```

- **用法**：`replace(old, new, count)`，`count`参数可选，表示替换的次数

### 5. `find()` 和 `index()`

**功能**：查找子字符串在字符串中首次出现的位置。

```python
text = "Hello, world!"
position = text.find("world")
# Output: 7
```

- **区别**：`find()` 找不到子字符串时返回 `-1`，`index()` 找不到时抛出 `ValueError`

### 6. `count()`

**功能**：返回子字符串在字符串中出现的次数。

```python
text = "Hello, world! Hello, everyone!"
count = text.count("Hello")
# Output: 2
```

### 7. `upper()` 和 `lower()`

**功能**：将字符串转换为大写或小写。

```python
text = "Hello, World!"
result = text.upper()
# Output: "HELLO, WORLD!"
```

### 8. `capitalize()` 和 `title()`

**功能**：将字符串的首字母或每个单词的首字母转换为大写。

```python
text = "hello, world!"
result = text.capitalize()
# Output: "Hello, world!"
```

### 9. `startswith()` 和 `endswith()`

**功能**：检查字符串是否以指定的前缀或后缀开头或结尾。

```python
text = "Hello, world!"
result = text.startswith("Hello")
# Output: True
```

### 10. `isnumeric()`, `isalpha()`, `isalnum()`, `isspace()`

**功能**：检查字符串是否只包含数字、字母、字母或数字、或空白字符。

```python
text = "12345"
result = text.isnumeric()
# Output: True
```

### 11. `format()` 和 f-string（格式化字符串）

**功能**：格式化字符串，插入变量值。

```python
name = "Alice"
age = 30
text = f"My name is {name} and I am {age} years old."
# Output: "My name is Alice and I am 30 years old."
```

### 12. `splitlines()`

**功能**：将字符串按行分割，返回一个包含各行的列表。

```python
text = "Hello\nworld!\nPython"
result = text.splitlines()
# Output: ['Hello', 'world!', 'Python']
```

### 13. `zfill()`

**功能**：在字符串左侧填充零，达到指定长度。

```python
text = "42"
result = text.zfill(5)
# Output: "00042"
```

### 14. `partition()` 和 `rpartition()`

**功能**：根据指定分隔符将字符串分为三部分：分隔符前、分隔符、分隔符后。

```python
text = "Hello, world!"
result = text.partition(", ")
# Output: ('Hello', ', ', 'world!')
```

### 15. `swapcase()`

**功能**：将字符串中的大写字母转换为小写，小写字母转换为大写。

```python
text = "Hello, World!"
result = text.swapcase()
# Output: "hELLO, wORLD!"
```

### 16. `expandtabs()`

**功能**：将字符串中的制表符（`\t`）替换为空格，默认使用8个空格的宽度。

```python
text = "Hello\tWorld!"
result = text.expandtabs(4)
# Output: "Hello   World!"
```

### 17. `maketrans()` 和 `translate()`

**功能**：用于字符映射替换。`maketrans()` 创建字符映射表，`translate()` 使用这个表进行替换。

```python
text = "hello world"
trans = str.maketrans("hlo", "jpa")
result = text.translate(trans)
# Output: "jeppe wprpd"
```

### 18. `casefold()`

**功能**：将字符串转换为小写，用于忽略大小写的比较。比 `lower()` 更加强大，能正确处理一些特殊情况（如德语的 ß）。

```python
text = "Hello, World!"
result = text.casefold()
# Output: "hello, world!"
```

### 19. `format_map()`

**功能**：与 `format()` 类似，但接受一个字典作为参数，用于插值。

```python
data = {'name': 'Alice', 'age': 30}
text = "My name is {name} and I am {age} years old.".format_map(data)
# Output: "My name is Alice and I am 30 years old."
```

### 20. `ljust()`, `rjust()`, 和 `center()`

**功能**：在字符串的左侧、右侧或两侧填充指定字符，使其达到指定长度。

```python
text = "Hello"
result = text.ljust(10, '-')
# Output: "Hello-----"

result = text.rjust(10, '-')
# Output: "-----Hello"

result = text.center(10, '-')
# Output: "--Hello---"
```

### 21. `isdecimal()`, `isdigit()`, 和 `isnumeric()`

**功能**：检查字符串是否仅包含十进制字符、数字字符或数值字符（包括分数和其他数值）。

```python
text = "12345"
result = text.isdecimal()  # True
result = text.isdigit()    # True
result = text.isnumeric()  # True
```

### 22. `encode()` 和 `decode()`

**功能**：将字符串编码为指定的字符编码格式（如 UTF-8），或从指定的字符编码格式解码为字符串。

```python
text = "Hello, world!"
encoded = text.encode('utf-8')
# Output: b'Hello, world!'

decoded = encoded.decode('utf-8')
# Output: "Hello, world!"
```

### 23. `isascii()`

**功能**：检查字符串是否只包含 ASCII 字符。

```python
text = "Hello"
result = text.isascii()
# Output: True
```

### 24. `removeprefix()` 和 `removesuffix()` (Python 3.9+)

**功能**：用于移除字符串的前缀或后缀。

```python
text = "Hello, world!"
result = text.removeprefix("Hello, ")
# Output: "world!"

result = text.removesuffix(" world!")
# Output: "Hello,"
```


### 25. `sorted(str)`

**功能**：返回一个包含字符串中字符的列表，按字母顺序排序（默认升序）。

```python
text = "hello"
result = sorted(text)
# Output: ['e', 'h', 'l', 'l', 'o']
```

- **用法**：`sorted(iterable, key=None, reverse=False)`
  - `iterable`：可以是字符串、列表等可迭代对象。
  - `key`（可选）：指定一个函数来执行自定义的排序。
  - `reverse`（可选）：如果为 `True`，则按降序排序。

**示例：**

```python
# 默认升序排序
text = "Python"
result = sorted(text)
# Output: ['P', 'h', 'n', 'o', 't', 'y']

# 自定义排序（按字符的ASCII码）
result = sorted(text, key=lambda x: ord(x))
# Output: ['P', 'h', 'n', 'o', 't', 'y']

# 降序排序
result = sorted(text, reverse=True)
# Output: ['y', 't', 'o', 'n', 'h', 'P']
```

**注意**：`sorted()` 不会修改原始字符串，而是返回一个新的列表。如果需要一个排序后的字符串，可以使用 `"".join(sorted(str))`。

**示例：**

```python
text = "Python"
sorted_text = "".join(sorted(text))
# Output: "Phnoty"
```
