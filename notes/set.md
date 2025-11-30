# 🐍 Sets in Python

**Definition**:  
A set in Python is an unordered, mutable collection of unique elements. Sets are useful for membership testing, eliminating duplicates, and performing mathematical set operations like union, intersection, and difference.

---

### 1. Creation and Syntax  
```python
s = {1, 2, 3}             # basic set
empty = set()             # empty set ({} creates a dict)
mixed = {1, "hello", 3.5} # heterogeneous set
from_list = set([1, 2, 2, 3])  # → {1, 2, 3}
```

---

### 2. Characteristics  
- **Unordered**: No index positions; elements have no fixed order.  
- **Unique elements**: Duplicates are automatically removed.  
- **Mutable**: Elements can be added or removed.  
- **Heterogeneous**: Can store different immutable types (numbers, strings, tuples).  
- **Not hashable**: Sets themselves cannot be dictionary keys, but their elements must be hashable.  

---

### 3. Membership and Iteration  
```python
s = {1, 2, 3}
1 in s        # → True
4 not in s    # → True

for item in s:
    print(item)
```

---

### 4. Common Methods with Syntax, Behavior, Edge Cases  

#### `.add(x)`  
```python
set.add(value)
```
- Adds element to set.  
- If already present, no effect.  

---

#### `.update(iterable)`  
```python
set.update(iterable)
```
- Adds multiple elements from iterable.  
- Duplicates ignored.  

---

#### `.remove(x)`  
```python
set.remove(value)
```
- Removes element.  
- **Edge case:** Raises `KeyError` if not found.  

---

#### `.discard(x)`  
```python
set.discard(value)
```
- Removes element if present.  
- **Edge case:** No error if not found.  

---

#### `.pop()`  
```python
set.pop()
```
- Removes and returns an arbitrary element.  
- **Edge case:** Raises `KeyError` if set empty.  

---

#### `.clear()`  
```python
set.clear()
```
- Removes all elements.  

---

#### `.copy()`  
```python
set.copy()
```
- Shallow copy.  

---

### 5. Mathematical Set Operations  

#### Union  
```python
a | b
a.union(b)
```
- Combines elements from both sets.  

#### Intersection  
```python
a & b
a.intersection(b)
```
- Elements common to both sets.  

#### Difference  
```python
a - b
a.difference(b)
```
- Elements in `a` but not in `b`.  

#### Symmetric Difference  
```python
a ^ b
a.symmetric_difference(b)
```
- Elements in either set but not both.  

---

### 6. Relational Methods  
```python
a.isdisjoint(b)   # True if no common elements
a.issubset(b)     # True if all elements of a in b
a.issuperset(b)   # True if a contains all elements of b
```

---

### 7. Built‑in Functions with Sets  
```python
len(s)       # number of elements
max(s), min(s)  # maximum/minimum element (requires comparable types)
sum(s)       # sum of numeric elements
sorted(s)    # returns a new sorted list
any(s)       # True if at least one element is truthy
all(s)       # True if all elements are truthy
set(iterable) # convert iterable to set
```

---

### 8. Frozen Sets  

**Definition**:  
A `frozenset` is an immutable version of a set. It supports membership tests and mathematical operations but cannot be modified.  

**Syntax**:  
```python
fs = frozenset([1, 2, 3])
empty_fs = frozenset()
```

**Characteristics**:  
- Immutable → no `.add()`, `.remove()`, `.discard()`, `.pop()`.  
- Hashable → can be dictionary keys or elements of another set.  

**Operations**:  
```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4])

a | b   # → frozenset({1, 2, 3, 4})
a & b   # → frozenset({3})
```

**Edge case**: Attempting mutating methods raises `AttributeError`.  

---

### 9. Edge Cases  
- `{}` creates dict, not set.  
- `remove()` raises `KeyError` if element absent; `discard()` avoids error.  
- `pop()` removes arbitrary element, not predictable.  
- Frozen sets cannot be modified.  

---

### 10. Use Cases  
- Removing duplicates from collections.  
- Membership testing (`in` / `not in`).  
- Mathematical set operations for data analysis.  
- Fast lookups compared to lists.  
- Frozen sets for immutability, dictionary keys, nested sets.  

---

## 🐍 Set Comprehensions in Python

**Definition**:  
A set comprehension is a concise way to construct a set using a single expression that combines iteration and optional filtering. It works like a list comprehension but produces a **set** (unordered, unique elements).

---

### 1. General Syntax  
```
{expression for item in iterable if condition}
```

- **expression** → the value to include in the set.  
- **item** → variable representing each element in the iterable.  
- **iterable** → sequence or collection to loop over.  
- **condition** (optional) → filter that decides whether to include the element.  

---

### 2. Basic Examples  
```python
# Squares of numbers
squares = {x**2 for x in range(5)}
# → {0, 1, 4, 9, 16}

# Unique characters from a string
chars = {c for c in "banana"}
# → {'b', 'a', 'n'}

# Filtering even numbers
evens = {x for x in range(10) if x % 2 == 0}
# → {0, 2, 4, 6, 8}
```

---

### 3. Nested Comprehensions  
```python
# Cartesian product as set of tuples
pairs = {(x, y) for x in [1, 2] for y in ['a', 'b']}
# → {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}
```

---

### 4. Edge Cases  
- **Duplicates removed automatically**:  
  ```python
  {x for x in [1, 1, 2, 2]}   # → {1, 2}
  ```
- **Empty iterable** → returns empty set:  
  ```python
  {x for x in []}   # → set()
  ```
- **Condition false for all** → empty set:  
  ```python
  {x for x in range(5) if x > 10}   # → set()
  ```
- **Unhashable elements not allowed**:  
  ```python
  { [1,2] for x in range(3) }   # TypeError: unhashable type: 'list'
  ```

---

### 5. Comparison with List Comprehensions  
- **List comprehension** → preserves order, allows duplicates.  
- **Set comprehension** → unordered, removes duplicates automatically.  

```python
[x for x in "banana"]   # → ['b', 'a', 'n', 'a', 'n', 'a']
{c for c in "banana"}   # → {'b', 'a', 'n'}
```

---


## 🔹 General Utility Note: `enumerate()`  

**Definition**:  
`enumerate()` is a built‑in function that adds an index counter to any iterable, commonly used in `for` loops.  

**Syntax**:  
```python
enumerate(iterable, start=0)
```

**Example**:  
```python
words = ["apple", "banana", "cherry"]
for i, w in enumerate(words, start=1):
    print(i, w)
# 1 apple
# 2 banana
# 3 cherry
```

---
