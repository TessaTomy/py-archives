# ✍️ Dictionaries in Python

**Definition**:  
A dictionary in Python is an unordered, mutable collection of key–value pairs. Keys must be hashable and unique, while values can be of any type. Dictionaries are optimized for fast lookups, insertions, and deletions.

---

### 1. Creation and Syntax  
```python
d = {"name": "Tessa", "age": 22}   # literal syntax
empty = {}                         # empty dict
empty2 = dict()                    # also empty dict
from_pairs = dict([("a", 1), ("b", 2)])  # from list of tuples
from_kwargs = dict(x=1, y=2)       # keyword arguments
```

---

### 2. Characteristics  
- **Unordered**: No guaranteed order before Python 3.7; insertion order preserved from 3.7+.  
- **Unique keys**: Duplicate keys overwrite previous values.  
- **Mutable**: Keys and values can be added, updated, or removed.  
- **Keys must be hashable**: Strings, numbers, tuples (immutable types). Lists/dicts cannot be keys.  
- **Values**: Can be any type, including other collections.  

---

### 3. Accessing Elements  
```python
d = {"a": 1, "b": 2}

d["a"]        # → 1
d.get("b")    # → 2
d.get("c")    # → None (safe, no error)
d.get("c", 0) # → 0 (default value)
```

- **Edge case**: `d["c"]` raises `KeyError` if key not found.  
- `.get()` avoids error, returns `None` or default.

---

### 4. Common Methods with Syntax, Behavior, Edge Cases  

#### `.keys()`  
```python
d.keys()
```
- Returns a view of keys.  
- Dynamic: reflects changes in dictionary.  

---

#### `.values()`  
```python
d.values()
```
- Returns a view of values.  

---

#### `.items()`  
```python
d.items()
```
- Returns a view of `(key, value)` pairs.  

---

#### `.update([other])`  
```python
d.update({"b": 99, "c": 3})
```
- Merges another dict or iterable of pairs.  
- Overwrites existing keys.  

---

#### `.pop(key[, default])`  
```python
d.pop("a")       # removes and returns value for "a"
d.pop("x", 0)    # returns 0 if "x" not found
```
- **Edge case**: Raises `KeyError` if key absent and no default provided.  

---

#### `.popitem()`  
```python
d.popitem()
```
- Removes and returns last inserted `(key, value)` pair.  
- **Edge case**: Raises `KeyError` if dict empty.  

---

#### `.setdefault(key[, default])`  
```python
d.setdefault("a", 0)   # returns value if key exists, else inserts default
```
- Useful for initializing keys.  

---

#### `.clear()`  
```python
d.clear()
```
- Removes all items.  

---

#### `.copy()`  
```python
d.copy()
```
- Shallow copy.  
- **Edge case**: Nested objects are shared.  

---

### 5. Dictionary Comprehensions  
**Syntax**:  
```
{key_expr: value_expr for item in iterable if condition}
```

**Examples**:  
```python
# Squares
squares = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering
evens = {x: "even" for x in range(10) if x % 2 == 0}
# → {0: 'even', 2: 'even', 4: 'even', 6: 'even', 8: 'even'}
```

---

### 6. Built‑in Functions with Dictionaries  
```python
len(d)       # number of key–value pairs
sorted(d)    # sorted list of keys
any(d)       # True if at least one key is truthy
all(d)       # True if all keys are truthy
```

---

### 7. Edge Cases  
- Duplicate keys overwrite values:  
  ```python
  {"a": 1, "a": 2}   # → {"a": 2}
  ```
- Keys must be hashable:  
  ```python
  {["x"]: 1}   # TypeError: unhashable type: 'list'
  ```
- `.popitem()` order: last inserted in Python 3.7+.  
- `.get()` avoids `KeyError`, unlike direct indexing.  

---
