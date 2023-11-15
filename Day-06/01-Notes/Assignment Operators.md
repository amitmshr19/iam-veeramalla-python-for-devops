# Assignment Operations in Python

## Introduction

Assignment operators in Python are used to assign values to variables. They include the basic assignment operator (=) and various compound assignment operators that perform an operation on the variable while assigning a value.

## List of Assignment Operators

1. **Basic Assignment (=):** Assigns a value to a variable.

2. **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.

3. **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.

4. **Multiplication Assignment (*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.

5. **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.

6. **Floor Division Assignment (//=):** Performs floor division on the left operand and assigns the result to the left operand.

7. **Modulus Assignment (%=):** Calculates the modulus of the left operand and assigns the result to the left operand.

8. **Exponentiation Assignment (**=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

## Examples

### Basic Assignment

```python
x = 5
```

### Addition Assignment

```python
y = 10
y += 3  # Equivalent to y = y + 3

###Certainly! Here are examples for each of the assignment operators you mentioned:

**# Addition assignment**
x = 5
y = 3
x += y
print(x)  # Output: 8
In this example, x += y is equivalent to x = x + y, so the value of x is updated to 5 + 3 = 8.


**# Subtraction assignment**
a = 10
b = 4
a -= b
print(a)  # Output: 6
Here, a -= b is equivalent to a = a - b, so the value of a is updated to 10 - 4 = 6.

**# Multiplication assignment**
p = 3
q = 6
p *= q
print(p)  # Output: 18
The statement p *= q is equivalent to p = p * q, so the value of p becomes 3 * 6 = 18.


**# Division assignment**
m = 20
n = 4
m /= n
print(m)  # Output: 5.0
Here, m /= n is equivalent to m = m / n, so the value of m is updated to 20 / 4 = 5.0. Note that the result is a floating-point number because regular division (/) in Python results in a float.
```

**# Floor division assignment**
p = 17
q = 5
p //= q
print(p)  # Output: 3
In this example, p //= q is equivalent to p = p // q, so the value of p is updated to the result of the floor division of 17 by 5, which is 3.

**# Modulus assignment**
a = 13
b = 4
a %= b
print(a)  # Output: 1
Here, a %= b is equivalent to a = a % b, so the value of a is updated to the remainder when 13 is divided by 4, which is 1.

**# Exponentiation assignment**
x = 2
y = 3
x **= y
print(x)  # Output: 8
The statement x **= y is equivalent to x = x ** y, so the value of x becomes 2 raised to the power of 3, which is 8.
