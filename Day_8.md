# File I/o in Python
<b>Python can be used to perform operations on a file. (read and write data)</b>

## Types of all files
1. Text Files: .txt, .docx, .log etc. 
2. Binary Files: .mp4, .mov, .png, .jpeg etc.

## Steps of a file operation
1. open a file 
2. Perform operations that are read or write 
3. Close the file

### Syntax 
f = open("File_name", "mode")<br><br>
where, mode: r, w <br>
File-name: sample.txt, dome.docx <br><br>

data = f.read()<br>
f.close()<br><br>

### Characters and their meaning in python

1. 'r': open for reading(default)
2. 'w': open for writing, truncating the file first
3. 'x': creating a new file and open it for writing 
4. 'a': open for writing, appending to the end of the file if it exists
5. 'b': binary mode
6. 't': text mode(default)
7. '+': open a disk file for updating (reading and writing)


### Reading a file
<b>Syntex:</b><br><br>
data = f.read() :- Reads entire file<br>
data = f.readline() :- reads one line at a time

### Writing to a file
f = open("demo.txt", "w")<br>
f.write("This is a new line") :-overwrites the entire file<br><br>

f= open("Demo.txt", "a")<br>
f.write("this is a new line") :-adds to the new file

### with Syntax
with open("demo.txt", "a") as f: <br>
data =f.read()

### Deleting a File
<b>Using the OS module</b><br>
<b>Module (like a code library) is file written by another programmer that generally has functions we can use.</b><br><br>

import os<br>
os.remove(fileName)