# 📋 _File Handling Notes_

**Notes on robust and efficient file interaction—covering resource management, access modes, and data persistence in Python.**

-----

## 1\. 📂 File Handling Fundamentals

Python file handling bridges the program and persistent storage. The entire operation is managed by a **File Object** (or handle), which acts as an interface.

  * **Primary Function:** **`open(file, mode)`**
      * **Purpose:** Establishes the connection and returns the file object.
      * **Arguments:** Requires the file path and a **mode** string (e.g., `'r'`, `'w'`, `'a'`).

-----

## 2\. 🔒 Context Management & The `with` Statement

The **`with` statement** is the highly recommended standard for file I/O. It utilizes the **Context Management Protocol** to ensure deterministic resource finalization.

### A. How `with` Guarantees Closure

The `with` statement guarantees that the file's **`close()`** method is called automatically upon exiting the block, even if an exception occurs.

  * **Significance:** This prevents **resource leaks** (leaving file handles open, which can exhaust system limits) and ensures the **I/O buffer is flushed** to the disk, safeguarding data integrity.

### B. Example of `with open()`

```python
# The file object is assigned to 'f' and is guaranteed to close
with open("data.txt", "w") as f:
    f.write("Data saved.")
# The file is now closed. Trying to access 'f' outside this block will fail.
```

### C. The Cost of Not Closing

If you use `f = open(...)` without a subsequent `f.close()`:

1.  **Resource Exhaustion:** Your program holds onto the file handle, which can lead to system-wide failure if too many files are opened concurrently.
2.  **Data Loss/Corruption:** Changes written to the file are often held in an **I/O buffer** by the operating system. They are only guaranteed to be written to the physical disk when the file is closed (`f.close()`) or the buffer is flushed (`f.flush()`). Failing to close means data loss if the program crashes.

-----

## 3\. 🎯 Detailed File Access Modes

The mode defines the operation type, the handling of non-existent files, and the initial pointer position.

| Mode | Purpose | Non-Existent File? | Pointer Position | Side Effect |
| :--- | :--- | :--- | :--- | :--- |
| **`r`** | **Read** | **Raises `FileNotFoundError`** | Start (Offset 0) | Read-only. |
| **`w`** | **Write** | **Creates file** | Start (Offset 0) | **TRUNCATES** (deletes all existing content). |
| **`a`** | **Append** | **Creates file** | End of File (EOF) | Preserves existing content. |
| **`x`** | **Exclusive Creation** | **Raises `FileExistsError`** | Start (Offset 0) | Fails if file exists; guarantees you are creating a new file. |
| **`r+`** | Read + Write | **Raises `FileNotFoundError`** | Start (Offset 0) | Allows both reading and overwriting. |
| **`w+`** | Write + Read | **Creates file** | Start (Offset 0) | **TRUNCATES** file, then allows reading/writing. |
| **`a+`** | Append + Read | **Creates file** | End of File (EOF) | Allows reading from start, but writes only to end. |

-----

## 4\. 📝 File Types and Error Handling

### A. File Types (`t` vs `b`)

The mode suffix determines how data is interpreted:

| Type | Mode Suffix | Purpose | Data Type | Encoding |
| :--- | :--- | :--- | :--- | :--- |
| **Text** | **`t`** (Default) | For standard text, code, or CSV files. | Strings (`str`) | Automatic encoding (usually UTF-8) and decoding. |
| **Binary** | **`b`** | For non-text data like images, audio, or executables. | Bytes (`bytes`) | No encoding/decoding is performed. |
| **XML Files** | **`t`** (Text) | XML files are plain text documents and are handled using standard text mode. | Strings (`str`) | Handled with standard text mode and often external XML parsing libraries. |

### B. Errors on Opening

  * **`FileNotFoundError`**: Occurs if you try to open a file with **read-only modes** (`r`, `r+`) or the **exclusive creation mode** (`x`) and the file does not exist.
  * **`FileExistsError`**: Occurs if you try to use the **exclusive creation mode** (`x`) and the file already exists.
  * **`PermissionError`**: Occurs if the operating system denies access (e.g., trying to write to a read-only directory or a file locked by another program).

-----

## 5\. ⚙️ Detailed File Object Methods

The following methods are called on the file object (`f`):

| Method | Purpose | Returns | Notes |
| :--- | :--- | :--- | :--- |
| **`f.write(s)`** | Writes the string `s` to the file. | Number of characters written. | Returns a `TypeError` if you try to write a string in binary mode (`'b'`). |
| **`f.writelines(lines)`** | Writes all strings in the iterable `lines`. | `None` | Does **not** add newline characters (`\n`). |
| **`f.read(n)`** | Reads and returns `n` characters/bytes. | String (`str`) or Bytes (`bytes`). | Reads entire file if `n` is omitted. |
| **`f.readline()`** | Reads and returns **one full line**. | String (`str`). | Returns an empty string (`''`) at the end of the file (EOF). |
| **`f.readlines()`** | Reads all lines into memory. | A **list of strings**. | Each string in the list includes the newline character (`\n`). |
| **`f.tell()`** | Reports the current file pointer position. | Integer offset. | |
| **`f.seek(offset)`** | Changes the file pointer position. | New position. | See Section 5 of the main notes for `whence` options. |
| **`f.truncate(size=None)`** | Resizes the file to the current pointer position or to `size`. | New size (integer). | **How to Remove Content:** To clear a file, open it in **`w`** mode; the truncation happens automatically upon opening. To truncate to a specific point, use `f.seek(pos)` followed by `f.truncate()`. |

-----

## **Note: Clearing a File Opened in Read/Write Mode (`'r+'`)**

When a file is opened in `'r+'` mode, it supports both reading and writing, and the file pointer starts at the beginning (offset 0). Crucially, this mode **does not automatically truncate** the file upon opening, meaning existing content is preserved.

To clear the content of a file opened in `'r+'` mode, you must explicitly use the **`truncate()`** method:

1.  **Move the Pointer to the Start:** Use **`f.seek(0)`** to reset the file pointer to the very beginning of the file.
2.  **Truncate:** Use **`f.truncate()`** to delete all content from the current pointer position (now the start of the file) to the end.

<!-- end list -->

```python
with open("filename.txt", "r+") as f:
    # Existing content is still present here.

    # 1. Move pointer to the start
    f.seek(0) 

    # 2. Truncate the file at the current pointer position (0)
    f.truncate()
    
    # The file content is now cleared
```
