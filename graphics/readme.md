# 📦 Graphics Package Setup

This project demonstrates how to create a modular Python package using folders, modules, and subpackages. The package is organized to support clean imports and reusable structure for 2D and 3D shape calculations.

## 🛠️ Steps to Create the Package

### 1. Create the Main Package Folder

```bash
mkdir graphics
cd graphics
```

### 2. Add Core Modules

```bash
touch __init__.py
touch rectangle.py
touch circle.py
```

### 3. Create a Subpackage for 3D Shapes

```bash
mkdir graphics_3d
cd graphics_3d
touch __init__.py
touch cuboid.py
touch sphere.py
```

### 4. Return to Root and Add Demo File

```bash
cd ../..
touch demo_graphics_package.py
```

## 📁 Final Folder Structure

```plaintext
graphics/
├── __init__.py
├── rectangle.py
├── circle.py
└── graphics_3d/
    ├── __init__.py
    ├── cuboid.py
    └── sphere.py
demo_graphics_package.py
```

## ⚙️ Setting Up `__init__.py` in Python Packages

To make a folder behave like a Python package, include an `__init__.py` file inside it. This file can be empty or used to expose specific modules and functions for clean imports.

### Exposing Submodules

Inside `mypackage/__init__.py`, you can expose modules like this:

```python
__all__ = ['module1', 'module2']

from . import module1
from . import module2
```

This allows:

```python
from mypackage import *
```

This enables:

```python
from mypackage.subpackage import *
```

---

This structure keeps your package modular, import-friendly, and ready for reuse or distribution.

## ✅ Notes

- `graphics` is the main package folder.
- `graphics_3d` is a subpackage inside `graphics`.
- Each module file (e.g., `rectangle.py`, `cuboid.py`) contains shape-related logic.
- `__init__.py` files are required to treat folders as packages.
- `demo_graphics_package.py` is used to demonstrate how to import and use the modules.

This setup supports modular imports like:

```python
from graphics import rectangle
from graphics.graphics_3d import cuboid
```
