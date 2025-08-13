

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) :  is used to interact with files on your system.


"""
f = open('demo.txt', 'r')

print(f)   # Output: <_io.TextIOWrapper name='C:/Users/USER/Documents/HH/Python/Lecture_10/demo.txt' mode='r' encoding='cp1252'>
# print(f.read())  # Output: First demo text file.

print(f.readline())  # Output: First demo text file.
print(f.readline())  # Output: (empty line)
print(f.readline())  # Output: (empty line)

f.close()
"""

#  ---------- Best way using 'with' syntax ---------- 
#  Writing file
with open('demo.txt', 'r') as f:
    data = f.read()
    print(data)  # Output: This is demo text file for python file I/O learning.



#  Updating file
with open('demo.txt', 'a') as f:
    data = f.write('Apended.')
    print(data)  # Output: 8



#  Deleting file
import os
os.remove('demo.txt')



#  Writing file
with open('demo.txt', 'w') as f:
    data = f.write('This is demo text file for python file I/O learning.')
    print(data)  # Output: 52


