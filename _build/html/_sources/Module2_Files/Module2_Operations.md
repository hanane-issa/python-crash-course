# M2: Operations

## 4 Operators and Expressions

**Expressions** are pieces of code that produce a value. They often involve **operators** – symbols or keywords that tell Python what kind of operation to perform.

### 4.1. Arithmetic Operators

| **Operator** |   **Description**   | **Example** | **Result** |
| :----------: | :-----------------: | :---------: | :--------: |
|      +       |      Addition       |    3 + 2    |     5      |
|      -       |     Subtraction     |    3 - 2    |     1      |
|      *       |   Multiplication    |    3 * 2    |     6      |
|      /       |  Division (float)   |    3 / 2    |    1.5     |
|      //      |   Floor Division    |   3 // 2    |     1      |
|      %       | Modulus (remainder) |    3 % 2    |     1      |
|      **      |   Exponentiation    |   3 ** 2    |     9      |

```python
a = 10
b = 3

sum_result = a + b # Output: 13
division_result = a / b # Output: 3.3333...
mod_result = a % b # Output: 1

print("Sum:", sum_result)
print("Division:", division_result)
print("Remainder:", mod_result)
```

### 4.2. Comparison Operators

Used to compute two values; the result is always a **Boolean** (`True` or `False`).

| **Operator** | **Description**  | **Example** | **Result** |
| :----------: | :--------------: | :---------: | :--------: |
|      ==      |     Equal to     |   3 == 2    |   False    |
|      !=      |   Not equal to   |   3 != 2    |    True    |
|      >       |   Greater than   |    3 > 2    |    True    |
|      <       |    Less than     |    3 < 2    |   False    |
|      >=      | Greater or equal |   3 >= 3    |    True    |
|      <=      |  Less or equal   |   3 <= 2    |   False    |

### 4.3. Logical Operators

Operate on **Boolean** values (`True` or `False`) and return also a **Boolean**.

| **Operator** |                **Description**                 |     **Example**     | **Result** |
| :----------: | :--------------------------------------------: | :-----------------: | :--------: |
|     and      |      True if **both** conditions are True      | (3 > 2) and (2 > 1) |    True    |
|      or      |   True if **at least one** condition is True   | (3 > 2) or (2 == 1) |    True    |
|     not      | Inverts the Boolean value (True becomes False) |     not (3 > 2)     |   False    |

```python
print((3 > 2) and (4 > 5)) # Output: False
print((2 < 5) or (10 < 3)) # Output: True
print(not (1 == 1)) # Output: False
```

### 4.4. Combining Operators into Expressions

You can combine multiple operators in a single expression. Python follows standard **order of operations** (sometimes called PEMDAS in math):
1. Parentheses.
2. Exponents
3. Multiplication / Division.
4. Addition / Subtraction.

```python
result = 3 + 5 * 2 # Multiplication done first => 3 + 10 = 13.
print(result)

parenthesized_result = (3 + 5) * 2 # Parentheses first => 8 * 2 = 16.
print(parenthesized_result)
```


---
