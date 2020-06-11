## Error Handling Research

### Murphy's Law

```
"Anything that can happen, will happen"
```

- Don't trust the user

### Syntax
#### try:
- Essentially "do this"

#### except_______:
- Unless this condition, in which case execute following line(s)

```python
while True:
    try:
        x = int(input("Please enter a number:  "))
        break
    except ValueError:
        print("That is not an integer")
```
- This code will ask the user to enter a number.
- If the user input is anything (including NoneType) other than an integer, a value error will be raised
- Then, for that instance, the except clause will execute
- Returned output will be: "That is not an integer"

#### raise:
- Allows an exception to be included when a condition is specified:

```python
while True:
    try:
        x = int(input("Please enter a number:  "))
        if x <= 10:
            break
        elif x > 10:
            raise Exception("Number too high")
    except ValueError:
        print("That is not an integer")
```
- Now if the integer is greater than 10, output will be: "Exception: Number too high"
- While loop will also break