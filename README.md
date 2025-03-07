# Swedish Learning Game UI

This project is part of the **Software Engineering and Project Management** course at **Uppsala University**. It focuses on developing the user interface (UI) for a Swedish learning game designed to help users learn Swedish interactively. This repository contains the code related to the Swedish Learning Game application, where users can practice Swedish through various levels and challenges.

## Application Setup

### Prerequisites
Before setting up the application, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)
- **MySQL**

### 1. Check if Python is Installed
To verify if Python is installed, open a terminal (or command prompt on Windows) and run the following command:

```bash
# macOS/Linux
python3 --version
```

```bash
# Windows
python --version
```

If Python is not installed, install it using the following:
- **macOS**:
```bash
  brew install python
```
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install python3
  ```
- **Windows**: Download and install it from [Python's official website](https://www.python.org/downloads/).

### 2. Check if pip is Installed

```bash
# macOS/Linux
pip3 --version
```

```bash
# Windows
pip --version
```

If pip is not installed, install it using:
```bash
# macOS/Linux
python3 -m ensurepip --upgrade
```

```bash
# Windows
python -m ensurepip --upgrade
```

### 3. Check if MySQL is Installed

```bash
# macOS/Linux
mysql --version
```

```bash
# Windows
mysql --version
```

If MySQL is not installed, install it using:

```bash
pip install mysql-connector-python
```

### 4. Check if Tkinter is Installed
To check if `tkinter` is installed, run:

```bash
python3 -m tkinter
```

If not installed, install it using:

- **macOS**:
 ```bash
  brew install python-tk
 ```

- **Linux**:
  ```bash
  sudo apt update
  sudo apt install python3-tk
  ```
- **Windows**: Tkinter should be available by default.

## Installation and Execution

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SamuelMoller/sepm-group6.git
   ```

2. Navigate to the project directory and start the application:
   ```bash
   python scripts/interface.py
   ```

