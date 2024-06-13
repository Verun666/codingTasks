# Sort and Search Algorithms

This repository contains implementations of various sorting and searching algorithms in Python, along with unit tests to ensure their correctness.

## Files

- `sort_and_search.py`: Contains the implementation of sorting and searching algorithms.
- `test_sort_and_search.py`: Contains unit tests for the algorithms in `sort_and_search.py`.

## Algorithms Implemented

The following algorithms are implemented in `sort_and_search.py`:
- **Sorting Algorithms:**
  - Insertion Sort

- **Searching Algorithms:**
  - Linear Search
  - Binary Search

## Requirements

To run the code and tests, you need to have Python installed. 
Ensure you have unittest installed, which is included in the Python standard library.

## Usage

### Running the Algorithms

You can import the algorithms from the sort_and_search module and use them in your Python code. Example:

```bash
from sort_and_search import binary_search

arr = [64, 34, 25, 12, 22, 11, 90]
number = 22
index = binary_search(arr, number)
print(f"Element {element} found at index {index}")
```

### Running the Unit Tests

To run the unit tests, use the following command:

```bash
python -m unittest test_sort_and_search.py
```

This will execute all the tests in test_sort_and_search.py and display the results.
