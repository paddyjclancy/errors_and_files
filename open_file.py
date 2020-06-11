
t = open("open_test.txt")

print("\n-read()")
print(t.read())

t = open("open_test.txt")

print("\n-readline()")
print(t.readline())

t = open("open_test.txt")

print("\n-for loop")
for u in t:
    print(u)