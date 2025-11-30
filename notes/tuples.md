# 📘 Collections in Python

Collections in Python are built‑in data structures that allow grouping, storing, and organizing multiple values efficiently. They include tuples, lists, sets, and dictionaries, each with distinct properties of mutability, ordering, and uniqueness. These structures are fundamental for handling complex data and are widely used in programming tasks.

---

# ✍️ Tuples in Python

**Definition**:  
A tuple in Python is an ordered, immutable collection of elements. Once created, the elements of a tuple cannot be modified, added, or removed. Tuples are often used to represent fixed data structures, group related values, and ensure data integrity.

---

### 1. Creation and Syntax  
- Tuples are defined using parentheses `()` or by simply separating values with commas.  
  ```python
  t1 = (1, 2, 3)
  t2 = "a", "b", "c"
  single = (5,)   # trailing comma required for single-element tuple
  ```
- Empty tuple: `empty = ()`

---

### 2. Characteristics  
- **Ordered**: Elements retain their position and can be accessed by index.  
- **Immutable**: Elements cannot be changed after creation.  
- **Heterogeneous**: Can store mixed data types (e.g., `(1, "hello", 3.5)`).  
- **Hashable**: Tuples can be used as dictionary keys if all their elements are immutable.  

---

### 3. Accessing Elements  
- Indexing: `t1[0] → 1`  
- Slicing: `t1[1:3] → (2, 3)`  
- Nested tuples: `nested = ((1,2), (3,4))`; `nested[0][1] → 2`

---

### 4. Operations  
- Concatenation: `(1,2) + (3,4) → (1,2,3,4)`  
- Repetition: `(1,2) * 2 → (1,2,1,2)`  
- Membership: `3 in (1,2,3) → True`  
- Iteration:  
  ```python
  for item in (1,2,3):
      print(item)
  ```

---

### 5. Methods and Functions  
- Tuples have limited methods due to immutability:  
  - `.count(value)` → returns occurrences of a value.  
  - `.index(value)` → returns the first index of a value.  
- Built‑in functions:  
  - `len(t)` → length of tuple.  
  - `max(t), min(t)` → maximum and minimum values.  
  - `sum(t)` → sum of numeric elements.  
  - `tuple(iterable)` → converts iterable into a tuple.

---

## 🔹 Named Tuples in Python

**Definition**:  
Named tuples are an extension of regular tuples provided by the `collections` module. They allow tuple elements to be accessed not only by index but also by name, improving readability and self‑documentation while retaining immutability and lightweight performance.

---

### 1. Creation and Syntax  
- Import from `collections`:  
  ```python
  from collections import namedtuple
  ```
- Define a named tuple type:  
  ```python
  Point = namedtuple("Point", ["x", "y"])
  ```
- Create instances:  
  ```python
  p1 = Point(10, 20)
  ```

---

### 2. Accessing Elements  
- By index: `p1[0] → 10`  
- By attribute name: `p1.x → 10`, `p1.y → 20`

---

### 3. Unpacking  
Unpacking means breaking a tuple (or named tuple) into individual variables in a single statement. This makes code cleaner and avoids manual indexing.  
```python
a, b = p1   # a = 10, b = 20
```
You can also use the “star” operator for extended unpacking:  
```python
Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student("Tessa", 22, "A")
n, *rest = s1   # n = "Tessa", rest = [22, "A"]
```
Unpacking is especially useful when functions return named tuples, allowing values to be assigned directly to meaningful variables.

---

Got it, Tessa — let’s focus **only on unpacking and the star operator** in Python, explained deeply and cleanly for your archive:

---

## 🔹 Unpacking and the Star Operator 

**Definition**:  
Unpacking is the process of assigning elements of a sequence (like a tuple, list, or named tuple) directly to variables in a single statement. It avoids manual indexing and makes code more readable. The **star operator (`*`)** extends unpacking by allowing one variable to capture multiple elements at once.

---

### 1. Basic Unpacking  
```python
t = (10, 20, 30)
a, b, c = t   # a=10, b=20, c=30
```
Each element of the tuple is assigned to a corresponding variable.

---

### 2. Star Operator in Unpacking  
The star operator groups remaining values into a list.  
```python
t = (1, 2, 3, 4, 5)

a, *rest = t       # a=1, rest=[2, 3, 4, 5]
*head, b = t       # head=[1, 2, 3, 4], b=5
x, y, *others = t  # x=1, y=2, others=[3, 4, 5]
```

---

### 3. Rules and Behavior  
- Only one starred variable is allowed in an unpacking assignment.  
- The starred variable always receives a **list**, even if it captures zero or one element.  
- Works with any iterable: tuples, lists, strings, ranges, named tuples.  
- Can be combined with normal unpacking for flexible assignments.

---

### 1. `*` Operator (Positional Expansion)  
When you use `*` on the **right‑hand side** inside a function call, it expands a sequence (like a tuple or list) into positional arguments.  
```python
def add(a, b, c):
    return a + b + c

nums = (1, 2, 3)
print(add(*nums))   # → 6
```

---

### 2. `**` Operator (Keyword Expansion)  
When you use `**` with a dictionary, it expands the dictionary into keyword arguments.  
```python
def greet(name, age):
    print(f"{name} is {age} years old")

info = {"name": "A", "age": 22}
greet(**info)   # → "A is 22 years old"
```
Here, the keys of the dictionary (`"name"`, `"age"`) become parameter names, and the values (`"A"`, `22`) are passed in.

---

### 3. Difference Between `*` and `**`  
- `*` → expands a sequence into **positional arguments**.  
- `**` → expands a dictionary into **keyword arguments**.  

---

