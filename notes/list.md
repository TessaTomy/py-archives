#  ✨Lists in Python

**Definition**:  
A list in Python is an ordered, mutable collection of elements. Lists can store heterogeneous data types, be resized dynamically, and support a wide range of operations. They are one of the most versatile and commonly used data structures in Python.

---

### 1. Creation and Syntax  
```python
nums = [1, 2, 3]                # basic list
words = ["apple", "banana"]     # list of strings
mixed = [1, "hello", 3.5]       # heterogeneous list
nested = [[1, 2], [3, 4]]       # nested list
lst = list("abc")               # convert iterable → ['a', 'b', 'c']
```

---

### 2. Characteristics  
- **Ordered**: Elements retain their position and can be accessed by index.  
- **Mutable**: Elements can be changed, added, or removed.  
- **Heterogeneous**: Can store different data types in the same list.  
- **Nested**: Lists can contain other lists.  

---

### 3. Indexing and Slicing Syntax  
General form:  
```
listname[start:stop:step]
```

Examples:  
```python
nums = [10, 20, 30, 40, 50]

nums[0]        # → 10        (first element)
nums[-1]       # → 50        (last element)
nums[1:4]      # → [20, 30, 40]   (slice from index 1 up to 3)
nums[:3]       # → [10, 20, 30]   (slice from start)
nums[2:]       # → [30, 40, 50]   (slice to end)
nums[::2]      # → [10, 30, 50]   (step of 2)
nums[::-1]     # → [50, 40, 30, 20, 10]   (reverse list)
```

---

### 4. Slice Assignment (Mutation)  
Lists are mutable, so slices can be replaced or removed:  
```python
nums = [1, 2, 3, 4, 5]

nums[1:3] = [99, 100]   # → [1, 99, 100, 4, 5]
nums[:2] = [7]          # → [7, 100, 4, 5]
nums[2:4] = []          # → [7, 100, 5]   (removes slice)

nums[::2] = [0, 0, 0]   # → [0, 100, 0, 4, 0]
nums[::2] = [9, 9]      # ValueError: length mismatch
```

---

### 5. Common Methods with Syntax, Behavior, Edge Cases

#### `.append(x)`  
```python
list.append(value)
```
- Adds element at end.  
- Always succeeds.  

---

#### `.extend(iterable)`  
```python
list.extend(iterable)
```
- Appends all elements from iterable.  
- If iterable raises during iteration, list may be partially modified.  

---

#### `.insert(i, x)`  
```python
list.insert(index, value)
```
- Inserts before position `index`.  
- `index <= 0` → inserts at start.  
- `index >= len(list)` → appends at end.  

---

#### `.remove(x)`  
```python
list.remove(value)
```
- Removes first occurrence of `value`.  
- **Edge case:** Raises `ValueError` if not found.  

---

#### `.pop([i])`  
```python
list.pop([index])
```
- Removes and returns element at `index`.  
- Default: last element.  
- **Edge case:** Raises `IndexError` if list empty or index out of range.  

---

#### `.clear()`  
```python
list.clear()
```
- Removes all elements.  

---

#### `.count(x)`  
```python
list.count(value)
```
- Returns number of occurrences.  
- Returns `0` if not found.  

---

#### `.index(x[, start[, stop]])`  
```python
list.index(value[, start[, stop]])
```
- Returns first index of `value`.  
- **Edge case:** Raises `ValueError` if not found.  
- Negative indices allowed.  

---

#### `.sort(key=None, reverse=False)`  
```python
list.sort(*, key=None, reverse=False)
```
- Sorts list in place; returns `None`.  
- Stable sort.  
- `key` is a function applied to elements.  
- `reverse=True` → descending order.  
- **Edge case:** Raises `TypeError` if elements not comparable. Exceptions in `key` propagate.  

Examples:  
```python
words = ['apple', 'Banana', 'cherry']
words.sort(key=str.lower)   # case-insensitive

pairs = [('alice', 3), ('bob', 1), ('carol', 2)]
pairs.sort(key=lambda p: p[1])  # sort by second element
```

---

#### `.reverse()`  
```python
list.reverse()
```
- Reverses list in place.  

---

#### `.copy()`  
```python
list.copy()
```
- Shallow copy.  
- **Edge case:** Nested objects are shared; use `copy.deepcopy` for deep copy.  

---

### 6. Built‑in Functions with Lists  
```python
len(lst)       # length
max(lst)       # maximum value
min(lst)       # minimum value
sum(lst)       # sum of numeric elements
sorted(lst)    # returns new sorted list
list(range(5)) # → [0, 1, 2, 3, 4]
```

---

Perfect, Tessa — let’s author a **complete, exam‑ready note on List Comprehensions** under Collections, with proper explanatory text, syntax blocks, examples, and edge cases. This will match the rhythm of your Tuples and Lists notes.

---

## List Comprehensions

**Definition**:  
A list comprehension is a concise way to create lists in Python using a single line of syntax that combines iteration, optional filtering, and expression evaluation. It is often more readable and efficient than using loops with `.append()`.

---

### 1. General Syntax  
```
[expression for item in iterable if condition]
```

- **expression** → the value to put in the list.  
- **item** → variable representing each element in the iterable.  
- **iterable** → sequence or collection to loop over.  
- **condition** (optional) → filter that decides whether to include the element.

---

### 2. Basic Examples  
```python
# Squares of numbers
squares = [x**2 for x in range(5)]  
# → [0, 1, 4, 9, 16]

# Filtering even numbers
evens = [x for x in range(10) if x % 2 == 0]  
# → [0, 2, 4, 6, 8]

# Strings to uppercase
words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]  
# → ['APPLE', 'BANANA', 'CHERRY']
```

---

### 3. Nested Comprehensions  
```python
# Flatten a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  
# → [1, 2, 3, 4, 5, 6]

# Cartesian product
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]  
# → [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

### 4. With Conditions  
```python
# Multiple conditions
nums = [x for x in range(20) if x % 2 == 0 if x > 10]  
# → [12, 14, 16, 18]

# Conditional expression inside comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]  
# → ['even', 'odd', 'even', 'odd', 'even']
```

---
