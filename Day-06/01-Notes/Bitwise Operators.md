# Bitwise Operations in Python

## Introduction

Bitwise operators in Python are used to perform operations on individual bits of binary numbers. These operators include bitwise AND, OR, XOR, and more.

## List of Bitwise Operators

1. **Bitwise AND (&):** Performs a bitwise AND operation on the binary representations of the operands.
2. **Bitwise OR (|):** Performs a bitwise OR operation.
3. **Bitwise XOR (^):** Performs a bitwise XOR operation.
4. **Bitwise NOT (~):** Flips the bits of the operand, changing 0 to 1 and 1 to 0.
5. **Left Shift (<<):** Shifts the bits to the left by a specified number of positions.
6. **Right Shift (>>):** Shifts the bits to the right.

## Examples

### Bitwise AND

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Result: 0001 (Decimal: 1)
```

### Bitwise OR

```python
x = 10  # Binary: 1010
y = 7   # Binary: 0111
result = x | y
# Result: 1111 (Decimal: 15)
```
### Certainly! Here are examples for both the bitwise AND (&) and bitwise OR (|) operations in Python:
# Bitwise AND operation
```python
a = 5   # binary: 0101
b = 3   # binary: 0011
result_and = a & b
print(result_and)
# Output: 1 (binary: 0001)
In this example, the bitwise AND operation is performed on the binary representations of a and b, resulting in 0001, which is 1 in decimal.
```

# Bitwise OR operation
```python
x = 10   # binary: 1010
y = 6    # binary: 0110
result_or = x | y
print(result_or)
# Output: 14 (binary: 1110)
Here, the bitwise OR operation is performed on the binary representations of x and y, resulting in 1110, which is 14 in decimal.
```

# Bitwise XOR operation
```python
m = 12   # binary: 1100
n = 7    # binary: 0111
result_xor = m ^ n
print(result_xor)
# Output: 11 (binary: 1011)
In this example, the bitwise XOR operation is performed on the binary representations of m and n, resulting in 1011, which is 11 in decimal.
```

# Bitwise NOT operation
```python
p = 8    # binary: 1000
result_not = ~p
print(result_not)
# Output: -9
Here, the bitwise NOT operation is performed on the binary representation of p, flipping the bits and resulting in -9 in decimal. Note that the result is represented using two's complement representation, which is a common way to represent signed integers in computers.
```

# Certainly! Here are examples for both the left shift (<<) and right shift (>>) operations in Python:
# Left shift operation
```python
x = 5    # binary: 0101
shifted_left = x << 2
print(shifted_left)
# Output: 20 (binary: 10100)
In this example, the bits of x are shifted to the left by 2 positions using the left shift operator (<<), resulting in 10100, which is 20 in decimal.
```

# Right shift operation
```python
y = 16   # binary: 10000
shifted_right = y >> 2
print(shifted_right)
# Output: 4 (binary: 00100)
Here, the bits of y are shifted to the right by 2 positions using the right shift operator (>>), resulting in 00100, which is 4 in decimal.
```
These bitwise shift operations are often used in low-level programming and can be useful in situations where you need to manipulate individual bits in binary representations of numbers.
---
