import os
num = int(input("Enter the size of the file: "))
name = []
with open('text.txt', 'w') as fp:
    for i in range(num):
        string = input("\nEnter the lines: ")
        name.append(string)
        fp.writelines(name)
size = os.stat('text.txt').st_size
if size == 0:
    print("file is empty")
else:
    print("file is full")
