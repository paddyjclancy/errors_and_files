
print("--------------\n-read()")

t = open("open_test.txt")
print(t.read())

print("--------------\n-readline()")

t = open("open_test.txt")
print(t.readline())

print("--------------\n-for loop")

t = open("open_test.txt")
for u in t:
    print(u)

print('--------------\n-Append - "a"')
# f = open("open_test.txt", "a")
# f.write("\nLine 4")
# f.close()
#
# g = open("open_test.txt")
# print(g.read())

print('--------------\n-Override - "w"')
# f = open("open_test.txt", "w")
# f.write("This will be the only text in the file")
# f.close()
#
# g = open("open_test.txt")
# print(g.read())

# Function
def open_and_print(file):
    o = open(file)
    print(o.read())

# open_and_print("open_test.txt")

def add_to_file(file, new_text):
    p = open(file, "a")
    p.write("\n" + new_text)
    p.close()
    q = open(file)
    print(q.read())

# add_to_file("open_test.txt", "Test")
