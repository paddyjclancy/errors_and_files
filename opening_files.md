## Opening files research
##### Within Python

- Process used to open files within the Python terminal
- Two stages: Opening and Reading

#### Open()
- First stage
- Returns the file object referenced, so it may then be read.
- Will need to be assigned to variable
- Once paired with a read(), will be complete

#### Read()
- Second stage
- Method tells the program to present the file to user.
- read() by default returns full file:

```python
t = open("open_test.txt")
print(t.read())
```
#### read(int)
- read(int) will return int number of characters.

#### readline()
- Will return one line of file only
- Can be repeated multiple times, to return multiple lines
```python
t = open("open_test.txt")
print(t.readline())
```

#### for loops
- Cleaner method of returning multiple lines of file

```python
t = open("open_test.txt")
for u in t:
    print(u)
```

### Writing
- Uses an extra parameter in the open() 
- "a" will APPEND
- "w" will WRITE / OVERRIDE
- write() instead of read()