
# 📃 Functions in Python  

**Definition**:  
A function in Python is a reusable block of code that performs a specific task. Functions improve modularity, readability, and reusability.  

---

### 1. Syntax of Function Definition  
```python
def function_name(parameters):
    """optional docstring"""
    # function body
    return value
```

- **`def`** → keyword to define a function.  
- **function_name** → identifier.  
- **parameters** → inputs (optional).  
- **return** → outputs (optional).  

---

### 2. Types of Functions  

- **Built‑in functions**: Provided by Python (`len()`, `print()`, etc.).  
- **User‑defined functions**: Created using `def`.  
- **Global functions**: Defined at module level, accessible anywhere.  
- **Local functions**: Defined inside another function, accessible only within.  
- **Lambda functions**: Anonymous, single‑expression functions.  
- **Recursive functions**: Functions that call themselves until a base condition is met.  

---

### 3. Scope of Variables  

- **Global variables**: Declared outside functions, accessible everywhere.  
- **Local variables**: Declared inside functions, accessible only within.  
- **`global` keyword**: Used to modify global variables inside a function.  

```python
x = 10  # global

def f():
    global x
    x = x + 1  # modifies global x
```

---

### 4. Formal vs Actual Parameters  

- **Formal parameters**: Declared in function definition.  
- **Actual parameters**: Values passed during function call.  

```python
def add(a, b):   # a, b → formal parameters
    return a + b

result = add(2, 3)  # 2, 3 → actual parameters
```

---

### 5. Errors with Parameters  

- **Too few arguments** → `TypeError`.  
  ```python
  def f(a, b): pass
  f(1)   # TypeError: missing 1 required positional argument
  ```
- **Too many arguments** → `TypeError`.  
  ```python
  f(1, 2, 3)   # TypeError: takes 2 positional arguments but 3 were given
  ```

---

### 6. Return Statement  

- **No return** → function returns `None`.  
  ```python
  def f(): pass
  print(f())   # → None
  ```
- **Return with no argument** → also returns `None`.  
  ```python
  def f(): return
  ```
- **Return single value** → returns that value.  
  ```python
  def f(): return 5
  ```
- **Return collection** → returns list, tuple, dict, etc.  
  ```python
  def f(): return [1, 2, 3]
  ```
- **Return comma‑separated values** → returns a tuple.  
  ```python
  def f(): return 1, 2, 3
  print(f())   # → (1, 2, 3)
  ```

---

### 7. Types of Arguments  

#### 1. Positional (Required) Arguments  
- Must be passed in correct order.  
```python
def greet(name, age):
    print(name, age)

greet("Tessa", 22)   # valid
greet(22, "Tessa")   # wrong order
```

#### 2. Keyword Arguments  
- Passed by name.  
```python
greet(age=22, name="Tessa")
```

#### 3. Default Arguments  
- Parameters with default values.  
```python
def greet(name, age=18):
    print(name, age)

greet("Tessa")       # → Tessa 18
```

#### 4. Variable‑length Arguments  
- **`*args`** → tuple of positional arguments.  
- **`**kwargs`** → dict of keyword arguments.  

```python
def f(*args, **kwargs):
    print(args)
    print(kwargs)

f(1, 2, 3, x=10, y=20)
# args → (1, 2, 3)
# kwargs → {'x': 10, 'y': 20}
```

---

### 8. Recursive Functions  

**Definition**: A function that calls itself until a base condition is met.  

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

factorial(5)   # → 120
```

- **Edge case**: Infinite recursion raises `RecursionError`.  

---

### 9. Lambda Functions  

**Definition**: Anonymous, single‑expression functions defined with `lambda`.  

**Syntax**:  
```python
lambda arguments: expression
```

**Examples**:  
```python
f = lambda x: x**2
print(f(5))   # → 25

add = lambda a, b: a + b
print(add(2, 3))   # → 5
```

**Characteristics**:  
- No `def`, no name (unless assigned).  
- Single expression only → no loops, branches, or multiple statements.  
- Implicit return → result of expression is returned.  
- Often used with `map()`, `filter()`, `sorted()`.  

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))   # → [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, nums))   # → [2, 4]
```

**Limitations**:  
- Cannot contain multiple statements.  
- Cannot include explicit loops or branching (`if`, `for`, `while`).  
- Best for short, throwaway functions.  

---

