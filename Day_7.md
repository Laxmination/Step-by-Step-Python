# Lists in Python
A built-in data type that stores set of values.<br> It can store elements of different types (integer, float, string, etc.)
<br>
Eg:<br>
marks = [87, 64, 33, 95, 76]<br>

student = [”Karan”, 85,“Delhi”]<br>

student[0] ="Karan"<br>


len(student) :- It returns length

# List Slicing
Accessing parts of a List.<br>
list_name[starting_idx:ending_idx] <br>
Eg: <br>
marks=[87, 64, 48, 11, 36, 88]<br>
marks[1:4] is [64, 48, 11]<br>
marks[ :4] is same as marks[0:4]<br>
marks[1: ] is same as marks[1:len(marks)]<br>
marks[-3:-1] is [11, 36]