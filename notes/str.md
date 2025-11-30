
# 📋 Strings in Python  

**Definition**:  
A string in Python is an immutable sequence of Unicode characters. Strings are widely used for text processing, storage, and manipulation.  

---

### 1. Creation and Syntax  
```python
s1 = "hello"          # double quotes
s2 = 'world'          # single quotes
s3 = """multi-line""" # triple quotes for multi-line
s4 = str(123)         # convert to string → "123"
```

---

### 2. Characteristics  
- **Immutable**: Strings cannot be changed after creation.  
- **Indexed**: Characters accessible by index.  
- **Iterable**: Can be looped over.  
- **Supports slicing**: Same syntax as lists.  

---

### 3. Indexing and Slicing  
General form:  
```
string[start:stop:step]
```

Examples:  
```python
s = "Python"

s[0]       # → 'P'
s[-1]      # → 'n'
s[1:4]     # → 'yth'
s[:3]      # → 'Pyt'
s[::2]     # → 'Pto'
s[::-1]    # → 'nohtyP'
```

---

### 4. Common Methods with Syntax, Behavior, Edge Cases  

#### `.upper()` / `.lower()`  
```python
s.upper()   # → 'PYTHON'
s.lower()   # → 'python'
```

#### `.strip()`  
```python
"  hi  ".strip()   # → 'hi'
```
- Removes whitespace (or specified chars) from both ends.
- lstrip() → left side only.
- rstrip() → right side only.
- strip() → both sides.

#### `.split(sep=None, maxsplit=-1)`  
```python
"a,b,c".split(",")   # → ['a', 'b', 'c']
```
- Splits into list.  
- **Edge case**: Default splits on whitespace.  

#### `.join(iterable)`  
```python
",".join(["a", "b", "c"])   # → 'a,b,c'
```
- Joins elements of iterable into string.  
- **Edge case**: Elements must be strings.  

#### `.find(sub[, start[, end]])`  
```python
"banana".find("na")   # → 2
"banana".find("x")    # → -1
```
- Returns lowest index or `-1` if not found.  

#### `.index(sub[, start[, end]])`  
```python
"banana".index("na")   # → 2
"banana".index("x")    # ValueError: substring not found
```
- Like `.find()`, but raises `ValueError` if not found.  

#### `.count(sub[, start[, end]])`  
```python
"banana".count("na")   # → 2
```
- Returns number of occurrences.  

#### `.replace(old, new[, count])`  
```python
"hello world".replace("world", "Python")   # → 'hello Python'
```

#### `.startswith(prefix)` / `.endswith(suffix)`  
```python
"Python".startswith("Py")   # → True
"Python".endswith("on")     # → True
```

---

### 5. String Formatting  

#### f‑strings (Python 3.6+)  
```python
name = "Tessa"
f"Hello, {name}!"   # → 'Hello, Tessa!'
```

#### `.format()`  
```python
"Hello, {}".format("world")   # → 'Hello, world'
```

#### Old `%` formatting  
```python
"Hello, %s" % "world"   # → 'Hello, world'
```

---

### 6. Escape Sequences  
```python
"Line1\nLine2"   # newline
"Tab\tSpace"     # tab
"Quote: \"text\"" # double quote inside string
```

---

### 7. Iteration and Membership  
```python
for ch in "abc":
    print(ch)

"x" in "text"    # → True
"z" not in "text" # → True
```

---

### 8. Edge Cases  
- Empty string: `""` has length 0, evaluates False in boolean context.  
- Strings are immutable: operations return new strings.  
- `.index()` raises `ValueError` if substring not found; `.find()` returns `-1`.  
- `.join()` requires all elements to be strings.  

---
